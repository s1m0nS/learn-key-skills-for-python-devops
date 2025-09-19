
## Step 1: Configure Development environment

* Configure GitHub Codespaces or the equivalent (Cloud9, etc)
* Create scaffold for structure of project: `Makefile` `requirements.txt`
* Optional (setup virtualenv) (install ipython outside requirements.txt) `pip install ipython`

## Step 2: Get interactive debugging working

* Use IPython and ipdb

```python
x = 1
y = 2
# import ipd; ipd.set_trace()
print( x + y)
```
