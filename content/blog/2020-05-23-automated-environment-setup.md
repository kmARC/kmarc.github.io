Title: Automated environment setup with direnv
Tags: kubernetes; shell; direnv

Config  files are  the past!  At least  for  server-side application  deployments. In  the docker  /
kubernetes world, where applications are deployed into ephemeral containers, we usually do not want
to bother mounting files into the containers, keeping them in sync across microservices, etc. In
kubernetes, especially when using the [sidecar pattern][], a container is executed with a lot of
environment variables conveniently set up.

[sidecar pattern]:https://kubernetes.io/blog/2015/06/the-distributed-system-toolkit-patterns/

Wanna bet? Check a simple app on kubernetes, the [dashboard][].

[dashboard]:https://github.com/kubernetes/dashboard "https://github.com/kubernetes/dashboard"

```bash
# Make sure you have a kubernetes env to work on
$ minikube start

# Deploy kubernetes-dashboard
$ kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.1/aio/deploy/recommended.yaml

# Run a temporary pod and check the number of automatically exported KUBERNETES_ variables
$ kubectl -n kubernetes-dashboard run --rm -ti --image=alpine temp
$ export | grep KUBERNETES_ | wc -l
# Output:
#    15
```

Just to make sure, you can check that the [deployment descriptor][] does not explicitly export any
of these variables.

[deployment descriptor]:https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.1/aio/deploy/recommended.yaml

Another example could be almost any of the docker images on docker hub. Check [MySQL][MySQL]; many of
the basics (that usually are environment dependent) are configurable via `MYSQL_` env vars.

[MySQL]:https://hub.docker.com/_/mysql/ "https://hub.docker.com/_/mysql/"


## Okay but what's the fuss with env vars anyway?

Nothing. You easily `export MY_VAR="42"` and `os.environ.get('MY_VAR')` in python
or `os.Getenv("MY_VAR")` in go. This is clear.

But now we talk about **a lot** of our configuration variables, URL endpoints of the microservices'
dependencies, switches that normally we add at runtime, and so on. Even a simple django application's
`settings.py` would explode over time with all the environment variables. It's easy then. Let's use
a different settings file in production than in testing, which in turn would be different than on
our development machine.

In the DevOps world, you do not want to have separate setting files[^1]. Industry best practice is
to use the same docker image in all the environments and "configure" the application through
environment variables.

[^1]:Or for that matter, you do not want **any** files to be different across environments

The question is...

## How to keep track of environment variables

I used to `source .env` whenever I `cd` into the root directory of my project. As long as you
remember to do this, you are fine. Oh, and you switch directories, you probably want to unload these
variables, right?

The answer to the problem of always forgetting to do so is [direnv][]. Direnv loads all your
environment variables when you `cd` into a directory, and unloads them when you leave.

It requires a one-time setup, and then you just need to get comfortable setting up your project
by simply creating a `.envrc` file where you can define your environment variables. Beware, once you
set this workflow up, it's becoming so convenient that you will miss it wherever you are _not_
allowed to install direnv...

## Show me an example!

Here you are. This works on Arch linux and bash, you might want to check the [official
documentation][] for other operating systems and shells.

[official documentation]:https://direnv.net/docs/installation.html

```bash
# Install direnv from AUR.
$ yay -S direnv

# Make sure direnv hooks are loaded.
$ echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
```

Reload / open a new shell now!

```bash
# Create and enter a project
$ mkdir my-project
$ cd !$

# Create your first .envrc
$ echo "export MY_VAR=42" >> .envrc
# Output:
#   direnv: error my-project/.envrc is blocked. Run `direnv allow` to approve its content
```

You got an  error message - direnv is blocked  in this directory, so it won't  load any arbitrary rc
files. Allow it!

```bash
$ direnv allow
# Output:
#   direnv: loading my-project/.envrc
#   direnv: export +MY_VAR
```

And that's it. as you can see, direnv took over and added (+) the MY_VAR variable to the
environment. You can check it yourself:

```bash
$ export | grep MY_VAR
# Output:
#   declare -x MY_VAR="42"
```

And now the automation magic comes: leave the `my-project` directory, and then come back to it, and
observe what happens:

```bash
$ cd ..
# Output:
#   direnv: unloading
$ export | grep MY_VAR
# No output, since MY_VAR is not defined anymore
$ cd -
# Output:
#   direnv: loading my-project/.envrc
#   direnv: export +MY_VAR
```

## Play around

Direnv is much more than just exporting env variables. It can bootstrap your python virtualenv,
select your node.js version, initialize PHP, Haskell, Go, and many other environments. No matter
what language/ecosystem you are working with, most probably you got covered - check the [wiki][]
for more information.

[wiki]:https://github.com/direnv/direnv/wiki "https://github.com/direnv/direnv/wiki"


[direnv]:https://direnv.net/ "https://direnv.net/"
