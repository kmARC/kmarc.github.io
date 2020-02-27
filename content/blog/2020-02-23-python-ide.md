title: My DevOps focused Python "IDE" (part I)
Tags: programming; vim; tmux; python

As from January 2020 I started a  new job at [Knowledge Lab](http://k-lab.ch/en/home), I again faced
the challenge of  how we could somehow  standardize tooling across team members  with a DevOps-first
approach, focusing on proper CI/CD infrastructure, code quality and automation wherever we can.

This post would be way too long if I covered everything here, thus the "part I" in the title.

## What's DevOps-first anyway?

Probably  the   reader  is   already  familiar   with  [the   Joel  test][joel-test],   the  [DevOps
Manifesto][devops-manifesto],  [The Twelve-Factor  App][twelve-factor] and  a million  random Medium
article that tells them how  to "do software" and how not to. These  are good resources, however, to
me all this DevOps hype boils down to one core principle:

> Automate. Everything.

As always, *everything* means a good 80-90% of... those things. Like... [Code coverage][].

[twelve-factor]:https://12factor.net/ "The Twelve factor app"
[devops-manifesto]:https://sites.google.com/a/jezhumble.net/devops-manifesto/ "DevOps Manifesto"
[joel-test]:https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/ "The Joel Test: 12 Steps to Better Code"
[Code coverage]:https://stackoverflow.com/questions/90002/what-is-a-reasonable-code-coverage-for-unit-tests-and-why

## What does it have to do with my IDE?

I saw way  too many people spending half their  lifetimes clicking around in PyCharm and  VS Code. I
would do the same: it's impossible to remember  all the obscure, random keyboard shortcuts. The only
reason <kbd>Ctrl</kbd>-<kbd>V</kbd>  stands for "paste" is  that <kbd>V</kbd> happens to  be next to
<kbd>C</kbd> on the keyboard [^querty].

The other problem is that sitting in front of  a slow-but-fancy IDE makes the programmer feel like a
pro, whereas  dozens of (pre-configured) plugins  are taking care  of the heavy work  of formatting,
linting, compiling, running  and testing[^devops] the code.

Guess  what,  these   actions  are  *exactly*  what   we  want  to  have  in   our  CI/CD  pipeline,
eventually. Thankfully CI/CD pipelines don't  build upon memory hog [IntelliJ][memory-intellij]s and
[VSCode][memory-vscode]s but the almost [50-year-old unix shells][unix].

## Learn you a shell for greater good!

There are a million resources  to learn [bash][] from. This article is not one  of those. If you are
comfortable with `cd` and `export`, know what `$PATH` is, you are good to go for now.

I'm going to show my setup in a couple of steps and then elaborate on each part with a bit of focus
on the newcomer. When I develop python et al, these are my requirements. Pick some of these you are
comfortable with and read on!

<img class="image-process-screenshot" alt="My IDE" src="{static}/pictures/python-ide.png"/>

1. **Automated environment setup**;  
   I go to the project folder and the environment automatically set up.
2. **Code & schema completion**;  
   While editing source code / deployment descriptors.
3. **Automated compiler, linter runs**;  
   Upon editing / saving source code.
4. **Automated test case runs**;  
   Upon editing test cases.
5. **Automated pre-commit checks for code QA**;
   I  want to  run  the  _same_ checks  locally  as  what's going  to  run on  the  gating  ci /  cd
   infrastructure.
6. **Documentation generator**; 
   What's displayed on git(Hub|Lab), I should be able to check rendered locally.
7. **Automated packaging**;  
   Again, I want to run the _same_ packaging procedure as what's on the ci/cd pipelint
6. Extra: **Entirely mouse free**;  
   Mouse slows you down: has only 3 buttons, requires 2D free cursor positioning, causes RSI.

As you can see, these involve a lot of (one-time) manual configuration; setting up the linters, code
coverage, commit hooks, environment variables. 

[^querty]:On a **QUERTY** keyboard, anyways...
[^devops]:... and analyzing code coverage, and dockerizing, and packaging, and signing, and
  integration testing, and... and...

[memory-intellij]: https://stackoverflow.com/search?q=intellij+memory "Random stackoverflow questions regarding IntelliJ's memory consumption"
[memory-vscode]: https://www.reddit.com/r/vscode/comments/c583zy/how_can_i_deal_with_the_massive_ram_usage_of/ "I like the answer: `Buy more RAM`"
[unix]: https://minnie.tuhs.org/cgi-bin/utree.pl?file=V6
[bash]: https://www.gnu.org/software/bash/
