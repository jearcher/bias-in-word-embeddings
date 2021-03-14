Use `unzip` or your favorite command to unzip the downloaded files
```
sudo apt install unzip
```

# Baseline


### Word2Vec: 

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

### Glove (Wikipedia 2014 + Gigaword 5) 322MB
```
curl -O http://nlp.stanford.edu/data/glove.6B.zip
unzip glove.6B.zip
```

GloVe (Common Crawl 840B): http://nlp.stanford.edu/data/glove.840B.300d.zip

### GloVe (Twitter 2B): http://nlp.stanford.edu/data/glove.twitter.27B.zip
```
curl -O http://nlp.stanford.edu/data/glove.twitter.27B.zip
unzip glove.twitter.27B.zip
mkdir glove.6B
mv glove.6B*.txt glove.6B
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


