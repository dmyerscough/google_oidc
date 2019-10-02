Google OIDC Token Generation
============================

Installing OIDC requirements
----------------------------

This script has a dependency on Google's Python modules, these can be installed using the following.

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install requirements.txt
```

Generating a OIDC token
-----------------------

In order to generate an OIDC token you must download a Google service account key and provide a OAuth Client ID:-

```bash
(env) $ python oidc_cli.py -f key.json -o 728761025347-ggaofgaopd6a055kcakkgvk0r4r3cs0d.apps.googleusercontent.com
```

* Minimal validation happens here, i'll add validation here at a later date
