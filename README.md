```bash
pip install -r requirements.txt
```


# BLEU evaluation
```bash
python bleu.py --ref my/ref.txt --hyp my/hyp.txt --max_order 4 --smooth False
```

```bash
python bleu.py --ref my/ref.txt --hyp my/hyp.txt --max_order 4 --smooth False
```
```python
import os, subprocess

ref = "my/ref.txt" 
hyp = "my/hyp.txt"

command = "multi-bleu.perl"
if os.name == "nt" :
    command = "perl %s" % command
p = subprocess.Popen(command % (ref, hyp), stdout=subprocess.PIPE, shell=True)
result = p.communicate()[0].decode("utf-8")
if result.startswith('BLEU'):
    bleu = float(result[7:result.index(',')])
else:
    print('Impossible to parse BLEU score! "%s"' % result)        
    bleu = -1
```