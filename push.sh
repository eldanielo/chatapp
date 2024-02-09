#!/bin/bash
git commit -am "autopush"
git push
npm run build
firebase deploy