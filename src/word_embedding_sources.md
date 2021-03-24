- Source directory is `bias-in-word-embeddings/data/embeddings/`
- Use `unzip` or your favorite command to unzip the downloaded files
```
sudo apt install unzip
```
- To download Google Drive Files (such as the original Google News Vectors for the Caliskan Paper), use the command `gdown`
(https://github.com/wkentaro/gdown)
```
pip install gdown
```
   
  
# Baseline


### Word2Vec: 
The main link `https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit` is not downloadable in the command line.
```
gdown https://drive.google.com/u/0/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download
```
This stops downloading after about 10 seconds
```
$ gdown https://drive.google.com/u/0/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download
[1] 4199
$ Downloading...
From: https://drive.google.com/u/0/uc?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM
To: /home/jearcher/jearcher/bias-in-word-embeddings/data/embeddings/GoogleNews-vectors-negative300.bin.gz
1.65GB [00:10, 162MB/s] 

```

### Glove (Wikipedia 2014 + Gigaword 5) 322MB
```
curl -O http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
mkdir glove.6B
mv glove.6B*.txt glove.6B
```

GloVe (Common Crawl 840B): http://nlp.stanford.edu/data/glove.840B.300d.zip

### GloVe (Twitter 2B): http://nlp.stanford.edu/data/glove.twitter.27B.zip
```
curl -O http://nlp.stanford.edu/data/glove.twitter.27B.zip
unzip glove.twitter.27B.zip
```

Returns an error: 
```
End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of glove.twitter.27B.zip or
        glove.twitter.27B.zip.zip, and cannot find glove.twitter.27B.zip.ZIP, period.
```

# New Embeddings (2019) 



Word-node2Vec (2019; Procheta Sen, Debasis Ganguly, Gareth Jones)
https://github.com/procheta/Word-Node2Vec


