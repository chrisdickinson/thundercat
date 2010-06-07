     .--------'                       .                            
    (_)   /    /                     /                         /   
         /    /-.  )  ( .  .-.  .-../   .-.  ).--..-.  .-. ---/--- 
        /    /   |(    ) )/   )(   /  ./.-'_/    (    (  |   /     
     .-/.__.'    | `--':'/   (  `-'-..(__.'/      `---'`-'-'/      
    (_/  `-                   `-                                   

thundercat, a client for nappingcat servers
===========================================
(as beta as it gets.)

Thundercat is a client command line program that interfaces with the latest versions
of nappingcat to provide github-like control over your repositories (but over the terminal!)

    thundercat addremote <nickname> <git url>

it will attempt to discover available commands for that new host, and store them in a JSON file
locally. When you run thundercat <nickname> <command and subcommands> it'll attempt to connect
to the server that nickname represents and run the corresponding command.


The side effect -- awesomeness (well, *hopefully*.) It becomes really easy to add permissions to
existing users from the comfort of your terminal:

    thundercat <nickname> add_permission garybusey kittygit read chris/test

will grant the user represented by "garybusey" the permission `('kittygit', 'read', 'chris/test')`
through the not-quite-so-cool-as-magic of nappingcat.


additionally, discoverable commands are parsed by `thundercat` as JSON so rich data will be (in theory)
available to the end-user -- including repository urls, so it's conceivable to add hooks to automatically
add git remotes when you create a repo on the server while inside a local git repository.

the results of commands run on the server will be colorized by their `status_code`, which roughly follows
HTTP status codes (I say roughly only because this needs a bit more work at the moment.)

Disclaimers
-----------
This is not anywhere near the prettiest code, nor should it be considered bullet-proof. It may undergo some
serious refactoring in the near futures. 

Also notable -- I'm borrowing the regex_helpers library from Django for the time being to provide a `reverse`-like
behavior for thundercat. Thanks (and sorry) guys!

Also, it's a command line program named after (the kid's tv show thundercats)[http://www.youtube.com/watch?v=P_cpV00c4IE],
so... you might have to live with that.
