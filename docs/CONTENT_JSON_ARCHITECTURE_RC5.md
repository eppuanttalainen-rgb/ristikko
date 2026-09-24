# RC5 content architecture

Sanaristeyksen päivittyvä ristikkosisältö on JSON-dataa.

Production path:
- app shell: index.html + app-config.js
- content: content/current.json
- content schema: sanaristeys-content / 1

Normaali sisältöjulkaisu:
Factory APPROVED_FOR_GAME_IMPORT -> JSON candidate builder -> validation -> current.json.

Native shell voi käyttää HTTPS current.json endpointia. Viimeinen validoitu paketti cachetetaan paikallisesti ja bundled baseline toimii viimeisenä fallbackina.

Tavoite: ristikoiden lisääminen ei vaadi sovelluskoodin eikä store-binaarin päivittämistä silloin, kun muutos on vain hyväksyttyä ristikkodataa.
