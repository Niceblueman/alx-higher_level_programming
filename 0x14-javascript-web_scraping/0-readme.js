#!/usr/bin/node
import { readFile } from 'node:fs';
readFile(process.argv[2], process.argv[3], 'utf-8', (err, data) => { err != null ? console.log(err): console.log(data); });
