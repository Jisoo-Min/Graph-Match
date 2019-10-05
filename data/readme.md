### Download solutions
We use java solutions in [github](https://github.com/mirandaio/codingbat) <br/>
Because it does not have **class definition**, we have to add calss definition. <br/>

After download it, run `make_class.py`. It automatically add code, while traversing directories.

```
python3 make_class.py
```

### Run PROGEX 



### Make Graph with basic blocks

You can make dot file and json file as an output. 
If you want to export a dot file, run below commmand
```
python3 make_basic_blocks.py [INPUT.json] dot
```

If you want to export a json file, run below commmand.
```
python3 make_basic_blocks.py [INPUT.json] json
```
It makes new directory which is named basic_blocks. In addition, it stores a graph file (.dot or .json) in basic_blocks directory.
