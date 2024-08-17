#!/bin/bash

echo "В директориии $PWD находится:"
ls -1 | du -sh * | sort -hr | more -5












