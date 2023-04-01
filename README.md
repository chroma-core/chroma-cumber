# chroma-cumber
the official chroma pickle wrapper

after working on [chroma](https://github.com/chroma-core/chroma) for several months now, 
the team has come to the realization that everything we were doing was
far too complicated for the task at hand 

embeddings? filtering? approximate nearest neighbor with iterative updates? 

no! far too complicated! 

what users really needed is a simple lightweight wrapper around a pickle.

chroma-cumber is that wrapper.  you're welcome. 

![pickle](F9D132BD-49F1-4540-82C6-FD2C7FC3A895.jpeg)

## Usage 

```python
from chroma-cumber import Chroma
```

then call your favorite `pickle` functions like `Chroma.dumps` and `Chroma.load`

it's full featured! 

thanks to [@typedfemale](https://twitter.com/typedfemale/status/1634307724904378368?s=46&t=Z-IqIba4nH3f1YLDFDKNPA) and [@deepfates](https://twitter.com/deepfates/status/1636247257782837248?s=46&t=Z-IqIba4nH3f1YLDFDKNPA) for the original concept and images. we could never have done it without you.  
