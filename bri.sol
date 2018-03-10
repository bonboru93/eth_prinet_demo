pragma solidity ^0.4.0;

contract Brightness
{
    address private owner;
    modifier isOwner()
    {
        require(msg.sender == owner);
        _;
    }
    
    function Brightness() public
    {
        owner = msg.sender;
    }
    
    int private bri = 0;
    function getBri() public view returns(int) {return bri;}
    function setBri(int _bri) public isOwner
    {
        bri = _bri;
    }
    
}