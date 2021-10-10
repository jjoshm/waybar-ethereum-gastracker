# waybar-ethereum-gastracker
Displays Ethereum Gas prices in your Waybar
Data is fetched from https://etherscan.io/gastracker

## Config
```
"custom/gas": {
        "exec": "gastracker.py",
        "return-type": "json"
}
```

You can define custom low/medium ranges for css classes:

```
"custom/gas": {
        "exec": "gastracker.py <low> <average>",
        "return-type": "json"
}
```
>average_price < `<low>` = low

>average_price < `<average>` = average

>average_price > `<average>` = high

for Example:
```
"custom/gas": {
        "exec": "gastracker.py 70 80",
        "return-type": "json"
}
```
>will set the `low` class if the average gas price is below 70, the `average` class if below 80 and the `high` class if above 80

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
