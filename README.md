# waybar-ethereum-gastracker
Script for the Waybar Custom Module https://github.com/Alexays/Waybar

Displays Ethereum Gas Price

Data is fetched from https://etherscan.io/gastracker

## Config
```
"custom/gas": {
        "exec": "gastracker.py",
        "return-type": "json"
}
```

## Styling
```
#custom-gas.low {
    background-color: green;
}

#custom-gas.average {
    background-color: #f1c40f;
}

#custom-gas.high {
    background-color: red;
}
```
>`high`is set when the average price is 10% higher the average price from the start time of the script.
>`low` is set when the average price is 10% lower the average price from the start time of the script
>.`average` everything between
