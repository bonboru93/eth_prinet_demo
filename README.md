# Ethereum private network with IoT device DEMO
## Network Topology
![network topology][1]
## Node Configuration

### PC1(Windows)

    [node1 init  ]geth --datadir=.\node1 init .\genesis.json
    [node1(archive node) start]geth --datadir=.\node1 --port 30303 --ipcpath node1 --nodiscover --gcmode=archive
    [node1 attach]geth attach ipc:\\.\pipe\node1
    [node1 wallet]".\Ethereum Wallet.exe" --rpc \\.\pipe\node1
    
    [node2 init  ]geth --datadir=.\node2 init .\genesis.json
    [node2 start ]geth --datadir=.\node2 --port 30304 --ipcpath node2 --nodiscover
    [node2 attach]geth attach ipc:\\.\pipe\node2
    [node2 wallet]".\Ethereum Wallet.exe" --rpc \\.\pipe\node2
    
### VM1, VM2(Ubuntu)

    [node3 init  ]./geth --datadir=./node3 init ./genesis.json
    [node3 start ]./geth --datadir=./node3 --nodiscover
    [node3 attach]./geth attach ./node3/geth.ipc
    [node3 wallet]ethereumwallet --rpc ./node3/geth.ipc
    
    [node4 init  ]./geth --datadir=./node4 init ./genesis.json
    [node4 start ]./geth --datadir=./node4 --nodiscover
    [node4 attach]./geth attach ./node4/geth.ipc
    [node4 wallet]ethereumwallet --rpc ./node4/geth.ipc

### PC2(Windows)
    [node5 init  ].\geth --datadir=.\node5 init .\genesis.json
    [node5 start ].\geth --datadir=.\node5 --nodiscover
    [node5 attach].\geth attach ipc:\\.\pipe
    [node5 wallet]".\Ethereum Wallet.exe"
    
### MacBook Pro
    [node6 init  ]./geth --datadir=./node6 init ./genesis.json
    [node6 start ]./geth --datadir=./node6 --nodiscover
    [node6 attach]./geth attach ./node6/geth.ipc
    [node6 wallet]/Application/Ethereum Wallet.app/Contents/MacOS/Ethereum Wallet --rpc ./node6/geth.ipc

### Raspberry Pi(Raspbian, armv7)

    [node_pi init ]./geth --datadir=./node_pi init ./genesis.json
    [node_pi start]./geth --datadir=./node_pi --nodiscover --rpc --rpcaddr 0.0.0.0 --rpcapi admin,debug,eth,miner,net,personal,rpc,txpool,web3
    [node6 attach ]./geth attach ./node_pi/geth.ipc
    [node6 wallet(connection from PC1)]".\Ethereum Wallet.exe" --rpc http://[NODE_PI IP]:8545
    
    [Download web3.py source code and compile, don't use 'pip install']
    
## Peer Connection

    [Under geth attached ipc console]
    src: admin.nodeInfo
    dst: admin.addPeer(enode://src_addr)
    
## Mining
    [Under geth attached ipc console]
    personal.newAccount()
    [Type passphrase]
    eth.coinbase
    miner.start(1)// 1 core

## Sample brightness reader

    briReader.py

## Sample ethereum poster

    ethPoster.py
    
## Sample monitor
    monitor.py


  [1]: https://github.com/bonboru93/eth_prinet_demo/blob/master/topology.JPG
