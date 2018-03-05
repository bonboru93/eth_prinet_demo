rd /s /q .\chaindata
rd /s /q %HOMEPATH%\AppData\Ethash
.\geth --datadir=./chaindata init .\genesis.json