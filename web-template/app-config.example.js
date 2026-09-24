// Example only. Production build is stored in the release handoff.
const APP_RELEASE_META = Object.freeze({
  appVersion: '0.3.41',
  releaseLabel: 'RC3',
  brand: 'Sanaristeys',
  subtitle: 'Suomalaiset ristikot',
  supportEmail: null
});

const MONETIZATION_CONFIG = Object.freeze({
  mode: 'none',
  adsEnabled: false,
  premiumEnabled: false,
  placements: Object.freeze({
    libraryNative: false,
    betweenPuzzles: false,
    rewardedHint: false
  }),
  premiumProducts: Object.freeze([])
});
