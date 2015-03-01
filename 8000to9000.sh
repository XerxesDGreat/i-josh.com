#!/bin/bash
outdir=$1
if [[ $outdir == '' ]]
then
    echo "need output dir"
    exit 1
fi
for f in `find ./${outputdir} -type f -iname \*.html`
do
    sed -e 's/localhost:8000/localhost:9000/g' $f > $f.tmp && mv $f.tmp $f
done
