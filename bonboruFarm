pragma solidity ^0.4.0;

contract BonboruFarm
{
    
    //OWNER
    address private owner;
    modifier isOwner()
    {
        require(msg.sender == owner);
        _;
    }
    
    uint private fieldPart;
    uint private producerPart;
    uint private expressPart;
    uint private sellerPart;
    function BonboruFarm(uint _fieldPart, uint _producerPart, uint _expressPart, uint _sellerPart) public payable
    {
        owner = msg.sender;
        fieldPart = _fieldPart;
        producerPart = _producerPart;
        expressPart = _expressPart;
        sellerPart = _sellerPart;
    }
    
    //FIELD
    struct Field
    {
        string name;
        string info;
        bool exist;
    }
    mapping (address => Field) private field;
    modifier isField()
    {
        require(field[msg.sender].exist);
        _;
    }
    function authField(address addr, string name, string info) public isOwner
    {
        field[addr] = Field(name, info, true);
    }
    struct FieldOutput
    {
        address fieldAddr;
        uint time;
        string comment;
    }
    FieldOutput[] private fieldOutput;
    event newFieldOutput(uint fieldOutputID, address producerAddr);
    function writeFieldOutput(uint time, string comment, address producerAddr) public isField
    {
        fieldOutput.push(FieldOutput(msg.sender, time, comment));
        newFieldOutput(fieldOutput.length - 1, producerAddr);
    }
    
    //PRODUCER
    struct Producer
    {
        string name;
        string info;
        bool exist;
    }
    mapping (address => Producer) private producer;
    modifier isProducer()
    {
        require(producer[msg.sender].exist);
        _;
    }
    function authProducer(address addr, string name, string info) public isOwner
    {
        producer[addr] = Producer(name, info, true);
    }
    struct ProducerOutput
    {
        address producerAddr;
        uint fieldOutputID;
        uint time;
        string comment;
    }
    ProducerOutput[] private producerOutput;
    event newProducerOutput(uint producerOutputID, address ExpressAddr);
    function writeProducerOutput(uint fieldOutputID, uint time, string comment, address ExpressAddr) public isProducer
    {
        producerOutput.push(ProducerOutput(msg.sender, fieldOutputID, time, comment));
        newProducerOutput(producerOutput.length - 1, ExpressAddr);
    }
    
    //EXPRESS
    struct Express
    {
        string name;
        string info;
        bool exist;
    }
    mapping (address => Express) private express;
    modifier isExpress()
    {
        require(express[msg.sender].exist);
        _;
    }
    function authExpress(address addr, string name, string info) public isOwner
    {
        express[addr] = Express(name, info, true);
    }
    struct ExpressOutput
    {
        address expressAddr;
        uint producerOutputID;
        uint time;
        string comment;
    }
    ExpressOutput[] private expressOutput;
    event newExpressOutput(uint expressOutputID, address SellerAddr);
    function writeExpressOutput(uint producerOutputID, uint time, string comment, address SellerAddr) public isExpress
    {
        expressOutput.push(ExpressOutput(msg.sender, producerOutputID, time, comment));
        newExpressOutput(expressOutput.length - 1, SellerAddr);
    }
    
    //SELLER
    struct Seller
    {
        string name;
        string info;
        bool exist;
    }
    mapping (address => Seller) private seller;
    modifier isSeller()
    {
        require(seller[msg.sender].exist);
        _;
    }
    function authSeller(address addr, string name, string info) public isOwner
    {
        seller[addr] = Seller(name, info, true);
    }
    struct SellerOutput
    {
        address sellerAddr;
        uint expressOutputID;
        uint time;
        uint price;
    }
    SellerOutput[] private sellerOutput;
    event newSellerOutput(uint sellerOutputID);
    function writeSellerOutput(uint expressOutputID, uint time, uint price) public isSeller
    {
        sellerOutput.push(SellerOutput(msg.sender, expressOutputID, time, price));
        newSellerOutput(sellerOutput.length - 1);
    }
    
    //BUYER
    function getLife(uint sellerOutputID) public view returns(
        string sellerInfo, 
        string expressInfo, string expressComment,
        string producerInfo, string producerComment,
        string fieldInfo, string fieldComment)
    {
        sellerInfo = seller[sellerOutput[sellerOutputID].sellerAddr].info;
        
        uint expressOutputID = sellerOutput[sellerOutputID].expressOutputID;
        expressInfo = express[expressOutput[expressOutputID].expressAddr].info;
        expressComment = expressOutput[expressOutputID].comment;
        
        uint producerOutputID = expressOutput[expressOutputID].producerOutputID;
        producerInfo = producer[producerOutput[producerOutputID].producerAddr].info;
        producerComment = producerOutput[producerOutputID].comment;
        
        uint fieldOutputID = producerOutput[producerOutputID].fieldOutputID;
        fieldInfo = field[fieldOutput[fieldOutputID].fieldAddr].info;
        fieldComment = fieldOutput[fieldOutputID].comment;
    }
    function buy(uint sellerOutputID) public payable
    {
        uint price = sellerOutput[sellerOutputID].price;
        require(msg.value >= price);
        
        address sellerAddr = sellerOutput[sellerOutputID].sellerAddr;
        sellerAddr.transfer(msg.value * sellerPart / 100);
        
        uint expressOutputID = sellerOutput[sellerOutputID].expressOutputID;
        address expressAddr = expressOutput[expressOutputID].expressAddr;
        expressAddr.transfer(msg.value * expressPart / 100);
        
        uint producerOutputID = expressOutput[expressOutputID].producerOutputID;
        address producerAddr = producerOutput[producerOutputID].producerAddr;
        producerAddr.transfer(msg.value * producerPart / 100);
        
        uint fieldOutputID = producerOutput[producerOutputID].fieldOutputID;
        address fieldAddr = fieldOutput[fieldOutputID].fieldAddr;
        fieldAddr.transfer(msg.value * fieldPart / 100);
    }
}