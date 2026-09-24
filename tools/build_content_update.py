#!/usr/bin/env python3
"""Build a reviewable next content pack from current.js + Factory approved_puzzles.json.

This tool does NOT publish anything. It validates duplicate IDs and creates a
candidate content file for the normal Sanaristeys editorial/regression gates.
"""
from pathlib import Path
import argparse, json, re, sys

ap=argparse.ArgumentParser()
ap.add_argument('--current',default='content/current.js')
ap.add_argument('--approved',required=True,help='Factory APPROVED_FOR_GAME_IMPORT JSON')
ap.add_argument('--new-version',required=True,help='e.g. 2026.2')
ap.add_argument('--out',default='content/next-candidate.js')
args=ap.parse_args()

src=Path(args.current).read_text(encoding='utf-8')
appr=json.loads(Path(args.approved).read_text(encoding='utf-8'))
puzzles=appr.get('puzzles') or appr.get('approvedPuzzles') or appr.get('approved_puzzles')
if not isinstance(puzzles,list) or not puzzles:
    sys.exit('Approved payload does not contain a non-empty puzzles list.')
new_ids=[p.get('id') for p in puzzles]
if any(not x for x in new_ids) or len(set(new_ids))!=len(new_ids):
    sys.exit('Approved batch has missing/duplicate IDs.')

m=re.search(r"(const PUZZLE_PACKS\s*=\s*\{\s*fi:\s*\[)(.*?)(\]\s*,\s*en:\s*\[\]\s*\};)",src,re.S)
if not m:
    sys.exit('Could not locate Finnish puzzle pack.')
for pid in new_ids:
    if re.search(r"\bid:\s*['\"]"+re.escape(pid)+r"['\"]",src):
        sys.exit(f'Puzzle ID already exists: {pid}')

def js(v):
    return json.dumps(v,ensure_ascii=False,separators=(',',':'))

append=',\n'+',\n'.join(js(p) for p in puzzles)+'\n'
new_src=src[:m.start(3)] + append + src[m.start(3):]

cm=re.search(r"const CURATED_PUZZLE_IDS\s*=\s*new Set\(\[(.*?)\]\);",new_src,re.S)
if not cm:
    sys.exit('Could not locate CURATED_PUZZLE_IDS.')
extra=','.join(js(x) for x in new_ids)
new_src=new_src[:cm.end(1)] + (',' if cm.group(1).strip() else '') + extra + new_src[cm.end(1):]

vm=re.search(r"visiblePuzzleCount:\s*(\d+)",new_src)
old_count=int(vm.group(1)) if vm else 0
old_ver=re.search(r"version:\s*['\"]([^'\"]+)['\"]",new_src).group(1)
new_src=re.sub(r"version:\s*['\"][^'\"]+['\"]",f"version: '{args.new_version}'",new_src,count=1)
new_src=re.sub(r"previousVersion:\s*(?:null|['\"][^'\"]+['\"])",f"previousVersion: '{old_ver}'",new_src,count=1)
new_src=re.sub(r"visiblePuzzleCount:\s*\d+",f"visiblePuzzleCount: {old_count+len(puzzles)}",new_src,count=1)
new_src=re.sub(r"addedPuzzleIds:\s*\[[^\]]*\]",'addedPuzzleIds: ['+','.join(js(x) for x in new_ids)+']',new_src,count=1)

Path(args.out).write_text(new_src,encoding='utf-8')
print(f'Wrote {args.out}: {old_count} -> {old_count+len(puzzles)} puzzles, content {old_ver} -> {args.new_version}')
