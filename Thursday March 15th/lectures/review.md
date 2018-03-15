## Review
We're going to review some recent concepts we've covered.

## Git
- Git vs GitHub  
- Clone vs Forking

## How do we add files
```
git status
git add <file_name>
git status
git commit -m "adding new file"
git status
git push
```

## What are virtualenvs
They are a fresh start without the weight of the baggage of your computer so you can install packages in isolation.

For macs:
```
virtualenv newvenv
source newvenv/bin/activate
```
For PCs:
```
virtualenv newenv
source first_env/Scripts/activate
```

## Internet!
- Internet is basically just a marriage of hardware and protocols.
- ARPANET - the grandfather to the internet. It’s just a network but the internet is a internet of internets. This started in the 1970s.
- The internet is always changing as new networks come and old ones go. There are satellite networks and land networks connected via submarine cables. This can be even as small as a home network, or local area network (like an office).
- The internet is made up of two types of machines clients and server. Every machine is ether a client or a server but many machines can be both.
- The client requests information from a server. The client starts with the local server and goes to a regional and than national server. It goes up the chain until it gets the information you need is.
- A server is a computer program or a device that provides functionality for other programs or devices(clients).
- When the information is being sent it needs to broken into many small pieces which are called packet. Packets don't always go in order and sometimes the same packets are sent separately in different places. Packets are reassembled based on the instructions that get sent.
- When you go to a website what happens?
The domain name system (DNS) translates hostnames such as (www.google.com) the ip address to a domain name. This happens via an DNS resolver.

# Requests

- HEAD - Same as GET but returns only HTTP headers and no document body
- PUT - Uploads a representation of the specified URI
- DELETE - Deletes the specified resource
- OPTIONS - Returns the HTTP methods that the server supports
- CONNECT - Converts the request connection to a transparent TCP/IP tunnel
