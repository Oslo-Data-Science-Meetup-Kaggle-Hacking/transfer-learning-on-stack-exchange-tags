# Transfer Learning on Stack Exchange Tags

by
[Oslo Data Science Meetup](https://www.meetup.com/Oslo-Data-Science/)
Kaggle Hacking Group,

A (WIP) solution to [transfer-learning-on-stack-exchange-tags](https://www.kaggle.com/c/transfer-learning-on-stack-exchange-tags/) on Kaggle.


## get data

```
$ pip install --user requirements.txt
$ cd data
$ ./get_data.py username
```

## read data

```
$ python -i read.py
>>> data['biology'][['title','tags']].head(5)
```

## clean data

```
$ python -i read.py
>>> data['biology'][['content', 'content_text']].head(10)
```
