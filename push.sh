#!/bin/bash
git commit -am "autopush"
git push
npm install
npm run build
firebase deploy