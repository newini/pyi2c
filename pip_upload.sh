#!/bin/bash

echo -e 'remove old dist files'
rm dist/*
echo -e ''
echo -e 'Building ...'
python3 -m build
echo -e ''
echo -e 'Uploading ...'
python3 -m twine upload dist/*
echo -e ''
