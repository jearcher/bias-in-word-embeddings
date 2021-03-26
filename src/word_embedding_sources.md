- Source directory is `bias-in-word-embeddings/data/embeddings/`
- Use `unzip` or your favorite command to unzip the downloaded files
```
sudo apt install unzip
```
- Mac and Linux can use the command `gzip` to unzip `.gz` files

- All pre-trained embeddings have been uploaded to a Google Cloud Bucket. The links to download .zip files are of the form:

```https://storage.googleapis.com/word-embedding-bias/FILEPATH```
   
  
# Baseline


### Word2Vec: 
The original link `https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit` is not downloadable in the command line.
```
mkdir Word2Vec

curl -o GoogleNews-vectors-negative300.bin.gz https://storage.googleapis.com/word-embedding-bias/Word2Vec/GoogleNews-vectors-negative300.bin.gz

gzip -d GoogleNews-vectors-negative300.bin.gz

cd .. 
```


### GloVe 

##### Wikipedia 2014 + Gigaword 5 (322MB). Original link: http://nlp.stanford.edu/data/glove.6B.zip

```
mkdir GloVe/
cd GloVe/
mkdir GloVe_6B/
cd GloVe_6B/
curl -O https://storage.googleapis.com/word-embedding-bias/GloVe/glove.6B.zip
unzip glove.6B.zip && rm glove.6B.zip 
cd ../
```

##### Common Crawl 840B. Original link: http://nlp.stanford.edu/data/glove.840B.300d.zip

```
curl -O https://storage.googleapis.com/word-embedding-bias/GloVe/glove.840B.300d.zip
unzip glove.840B.300d.zip 
rm glove.840B.300d.zip
```

##### Twitter 27B. Original link: http://nlp.stanford.edu/data/glove.twitter.27B.zip

```
mkdir GloVe_twitter_27B/ && cd GloVe_twitter_27B/
curl -O https://storage.googleapis.com/word-embedding-bias/GloVe/glove.twitter.27B.zip
unzip glove.twitter.27B.zip && rm glove.twitter.27B.zip
cd ../
```



# New Embeddings (2019) 



Word-node2Vec (2019; Procheta Sen, Debasis Ganguly, Gareth Jones)
https://github.com/procheta/Word-Node2Vec


