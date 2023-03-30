# Alpaca.cpp (Alpaca-zh, For Chinese)

Run a fast ChatGPT-like model locally on your device, use baidu fanyi api to translate from/to Chinese. 
The screencast below is not sped up and running on an M1 Macbook Pro  with 8GB of weights. 

[![asciicast](screencast.gif)](https://asciinema.org/a/dfJ8QXZ4u978Ona59LPEldtKK)


## Forked From:

This forked from 
[chat CLI](https://github.com/antimatter15/alpaca.cpp), which combine:
[LLaMA foundation model](https://github.com/facebookresearch/llama) 
[open reproduction](https://github.com/tloen/alpaca-lora)
[Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca)
[RLHF](https://huggingface.co/blog/rlhf)
[llama.cpp](https://github.com/ggerganov/llama.cpp)

## Changed 

1. Add Baidu fanyi() to translate from Question, and to Answer, between English & Chinese
2. Change the Command Line(interactive mode) to use Chinese & English more comfortably.
3. Add 'help', 'exit', 'quit', 'trans', 'notrans' etc. in Command Line to quit or change mode.

## Get Started (7B)

Get the appid & secretkey from baidu(http://api.fanyi.baidu.com, Personal for free)

Get the model file:

Download `ggml-alpaca-7b-q4.bin` and place it in the same folder as the `chat`, which can be got from:
https://huggingface.co/Sosaka/Alpaca-native-4bit-ggml/blob/main/ggml-alpaca-7b-q4.bin 

Once you've downloaded the model weights and placed them into the same directory as the `chat` or `chat.exe` executable, run:

```
./chat
```

The weights are based on the published fine-tunes from `alpaca-lora`, converted back into a pytorch checkpoint with a [modified script](https://github.com/tloen/alpaca-lora/pull/19) and then quantized with llama.cpp the regular way. 

## Building from Source (MacOS/Linux)


```sh
git clone https://github.com/thinkahead123/alpaca.cpp
cd alpaca.cpp

# if you use macbook pro M1, may be found when running ./chat
#  1. cause 'illegal hardware instruction'
#  2. running speed is very slowly
# there are bugs in compiling,  use the copy firstly to cover old one
# cp ./CMakeLists.MBP_M1.txt ./CMakeLists.txt
#
cmake .
make chat
./chat
```


## Building from Source (Windows)

- Download and install CMake: <https://cmake.org/download/>
- Download and install `git`. If you've never used git before, consider a GUI client like <https://desktop.github.com/>
- Clone this repo using your git client of choice (for GitHub Desktop, go to File -> Clone repository -> From URL and paste `https://github.com/thinkahead123/alpaca.cpp` in as the URL)
- Open a Windows Terminal inside the folder you cloned the repository to
- Run the following commands one by one:

```ps1
cmake .
cmake --build . --config Release
```

- Download the weights via any of the links in "Get started" above, and save the file as `ggml-alpaca-7b-q4.bin` in the main Alpaca directory.
- In the terminal window, run this command:
```ps1
.\Release\chat.exe
```
- (You can add other launch options like `--n 8` as preferred onto the same line)
- You can now type to the AI in the terminal and it will reply. Enjoy!

## Credit

This combines [Facebook's LLaMA](https://github.com/facebookresearch/llama), [Stanford Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html), [alpaca-lora](https://github.com/tloen/alpaca-lora) and [corresponding weights](https://huggingface.co/tloen/alpaca-lora-7b/tree/main) by Eric Wang (which uses [Jason Phang's implementation of LLaMA](https://github.com/huggingface/transformers/pull/21955) on top of Hugging Face Transformers), and [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov. The chat implementation is based on Matvey Soloviev's [Interactive Mode](https://github.com/ggerganov/llama.cpp/pull/61) for llama.cpp. Inspired by [Simon Willison's](https://til.simonwillison.net/llms/llama-7b-m2) getting started guide for LLaMA. [Andy Matuschak](https://twitter.com/andy_matuschak/status/1636769182066053120)'s thread on adapting this to 13B, using fine tuning weights by [Sam Witteveen](https://huggingface.co/samwit/alpaca13B-lora). 


## Disclaimer

Note that the model weights are only to be used for research purposes, as they are derivative of LLaMA, and uses the published instruction data from the Stanford Alpaca project which is generated by OpenAI, which itself disallows the usage of its outputs to train competing models. 


