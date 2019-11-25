# Introduction

Flask based API server for autocompletion

# Structure

```bash
.
├── README.md
├── api
│   ├── __init__.py
│   ├── hello_api.py
│   ├── law_api.py
│   ├── opinion_api.py
│   └── term_api.py
├── application.yml
├── config
│   └── __init__.py
├── db
│   ├── __init__.py
│   └── mongodb.py
├── requirements.txt
├── service
│   ├── __init__.py
│   ├── hello_service.py
│   ├── law_service.py
│   ├── opinion_service.py
│   └── term_service.py
├── start.py
└── start.sh

# /api - api 
# /service - services that could be called by api
# /config - all configuration
# application.yml - serve as a setting file (Empty now for simplicity)
# start.py - main file
```

# API

There are three kinds of api here.

1. term_api
2. law_api
3. opinion_api

```bash
# Format
https://<IP>:<PORT>/autocomplete/api/<VERSION>/<API_NAME>

# Term API
https://127.0.0.1:47000/autocomplete/api/v1/term

# Law API
https://127.0.0.1:47000/autocomplete/api/v1/law

# Opinion API
https://127.0.0.1:47000/autocomplete/api/v1/opinion

```

# Func 1: term api

Request:

```bash
$ curl -X POST \
-H "Content-Type: application/json" \
-d '{"keyword" : '法', "complete" : true, "limit": 5}' \
"http://127.0.0.1:47000/autocomplete/api/v1/term"

```

Response:

```bash
{
    "data":{
        "count": 1
        "isFound": true
        "keyword": "法"
        "terms": ["法律"]
    },
    "message": "Success",
    "errorCode": "000"
}
```

# Func 2: law api

Request:

```bash
$ curl -X POST \
-H "Content-Type: application/json" \
-d '{"keyword" : '專利', "complete" : true, "limit": 5}' \
"http://127.0.0.1:47000/autocomplete/api/v1/law"

```

Response:

```bash
{
    "data":{
        "count": 5
        "isFound": true
        "keyword": "專利"
        "laws": [{
                "description": "為鼓勵、保護、利用發明、新型及設計之創作，以促進產業發展，特制定本法。",
                "name": "專利法第1條",
                ...
            }]
    },
    "message": "Success",
    "errorCode": "000"
}
```

# Func 3 : opinion api

Request:

```bash
$ curl -X POST \
-H "Content-Type: application/json" \
-d '{"keyword" : '新型', "complete" : true, "limit": 5}' \
"http://127.0.0.1:47000/autocomplete/api/v1/opinion"

```

Response:

```bash
{
    "data":{
        "count": 3
        "isFound": true
        "keyword": "新型"
        "opinions": [
            {
                "concept": "新型專利",
                "count": 4,
                "descriptions": [
                    "專利法於92年2月6日修正公布全文138條，就新型專利改採形式審查，對新型專利申請案僅為形式要件之審查，而不進行前案檢索及實體要件之判斷（如產業利用性、新穎性、進步性等）。惟考量僅經形式審查所取得之新型專利權，其權利內容具有不安定性及不確定性，為免新型專利權人不當權利行使，有害於第三人之技術利用及研發，特於第103條至第105條增訂「新型專利技術報告」制度，促使新型專利權人妥適行使權利，且供公眾得以判斷新型專利是否符合實體要件，而具有公眾審查之功能。準此，新型專利技術報告僅為申請人判斷該新型專利權是否合於專利實體要件之參考，以及新型專利權人行使權利之佐證，非謂專利權人於新型專利公告後即應申請新型專利技術報告始能維護其專利權(智慧財產法院100年度民專上字第53號判決)",
                    ...
                ]
            },
            {
                "concept": "新型專利標的",
                "count": 1,
                "descriptions": [
                    "申請新型之標的，應屬對物品之「形狀」（指物品具有可從外觀觀察到確定之空間輪廓者）、「構造」（指物品內部或其整體之構成，實質表現上大多為各組成元件間之安排、配置及相互關係，且此構造之各組成元件並非以其本身原有之機能獨立運作者）或「裝置」（指為達到某一特定目的，將原具有單獨使用機能之多數獨立物品予以組合裝設者）之創作。至於物之製造方法、使用方法、處理方法等，及無一定空間形狀、構造的化學物質或醫藥品，甚至以美感為目的之物品形狀、花紋、色彩或其結合等創作，均非新型之標的，即不得依申請取得新型專利。(智慧財產法院101年度民專訴字第11號判決)"
                ]
            },
            {
                ...
            }

    },
    "message": "Success",
    "errorCode": "000"
}
```

# ErrorCode

1. 001 - ValueError
2. 002 - TypeError
3. 999 - Unexpected Error
4. 000 - Success

# Author

All codes are created from scratch by tsupei(tsupei0527@gmail.com). 





