#!/bin/bash
rm -f iServStorARC.tar.gz iServStorPKG.tar.gz
sudo ntpdate time.stdtime.gov.tw
path="http://140.92.143.210/release/iservstor"
for i in "iServStorARC" "iServStorPKG"; do
    wget --http-user=iservstor --http-passwd=iservstor $path/${i}.tar.gz
done
tar zxf iServStorPKG.tar.gz
cp iservstor.rc iServStorPKG
cd iServStorPKG
chmod +x deploy
#./deploy install
