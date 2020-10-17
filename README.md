
# flipdirs

Adott egy csomó fájl, amiket _két_ szempont -- `A` és `B` --
szerint értelmes osztályozni.
Hogyan rendezzük el őket egy könyvtárstrukturában?
Az alaplehetőség az, hogy `A` szerint csinálunk
könyvtárakat és _azon belül_ `B` szempont szerint alkönyvtárakat.
De akkor hogyan tudunk kényelmesen a `B` szempont szerint,
azaz fordított logikával keresni?
Létrehozzuk a kifordított könyvtárstrukturát is,
amiben először `B` szerint és aztán `A` szerint osztályozunk.

Ez a program utóbbinak a létrehozását automatizálja.
(1) kialakítja a kifordított könyvtárstrukturát;
(2) symlinkeket helyez el benne a megfelelő fájlokra;
(3) az eredeti `inner_READMEs` könyvtárban elhelyezett `README`
fájlokat is belinkeli a megfelelő helyre.

A kifordított könyvtárstrukturát rendszeresen újra lehet generálni,
akár `cron`-ból, és így az eredeti mellett
automatikusan és folyamatosan biztosítani lehet
a fordított logikájú hozzáférést is.

## input

`make create_dirs` által készítünk el egy kiinduló könyvtárstrukturát:

```txt
├── corpora
│   ├── corpus1
│   │   ├── noske
│   │   │   └── corpus1.noske
│   │   ├── raw
│   │   │   └── corpus1.raw
│   │   ├── README.md
│   │   └── spl
│   │       └── corpus1.spl
│   ├── corpus2
│   │   ├── raw
│   │   │   └── corpus2.raw
│   │   ├── README.md
│   │   └── spl
│   ├── corpus3
│   │   ├── raw
│   │   └── README.md
│   └── inner_READMEs
│       ├── README.raw.md
│       └── README.spl.md
```

## output

`make flip_dirs` által készítjük el belőle a kifordított verziót:

```txt
├── corpora_by_format
│   ├── noske
│   │   ├── corpus1 -> ../../corpora/corpus1/noske
│   │   └── README.noske.md -> ../../corpora/inner_READMEs/README.noske.md
│   ├── raw
│   │   ├── corpus1 -> ../../corpora/corpus1/raw
│   │   ├── corpus2 -> ../../corpora/corpus2/raw
│   │   ├── corpus3 -> ../../corpora/corpus3/raw
│   │   └── README.raw.md -> ../../corpora/inner_READMEs/README.raw.md
│   └── spl
│       ├── corpus1 -> ../../corpora/corpus1/spl
│       ├── corpus2 -> ../../corpora/corpus2/spl
│       └── README.spl.md -> ../../corpora/inner_READMEs/README.spl.md
```

