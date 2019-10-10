some of data to use are already uploaded to the folder. In addition, the flow that can generate data is described below. However, you can use the data that exists in the basic_blocks folder immediately without running the following executable commands.

### 1. Download solution codes and Append class definition
We use java solutions in [github](https://github.com/mirandaio/codingbat) <br/>
Because it does not have **class definition** to use PROGEX, we have to add class definition. <br/>

After download it, run `make_class.py`. It automatically add code, while traversing directories.

From root directory of this repository,
```sh
cd data
git clone https://github.com/mirandaio/codingbat
python3 make_class.py
```
Then, all sources are in the codingbat-data folder with class definition. 

### 2. Run PROGEX
```sh
cd progex-result
./run_progex.sh
```

### 3. Make Graph with basic blocks
You can make dot file and json file as an output. If you want to export a dot file, run below commmands.

From root directory of this repository,
```sh
cd data
```

* If you want to export a json file, run below commmand.
```sh
python3 make_basic_blocks.py [path/file_name.json] dot
```

* If you want to export a json file, run below commmand.
```sh
python3 make_basic_blocks.py [path/file_name.json] json
```

* If you want to recursively export json files, run below command.
```sh
./run_make_basic_blocks.sh [json or dot]
````
It makes new directory which is named basic_blocks. In addition, it stores a graph file (.dot or .json) in basic_blocks directory.
