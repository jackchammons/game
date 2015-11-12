import sys

from twisted.internet import reactor
from twisted.python import log
from twisted.web.server import Site
from twisted.web.static import File

from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol

from autobahn.twisted.resource import WebSocketResource


import json


class Update(object):
    def __init__(self, userID, username):
        self.userID = userID
        self.username = username



class Structure(object):
    def __init__(self, structureID, structureType, location, )
        self.structureID = structureID
        self.type = structureType



class Player(object):
    def __init__(self, userID, username, inGame, currentGame)


class Game(object):
    def __init__(self, gameID, players, structures, ships)


    def destroyStructure





def object_decoder(obj):
    #check if this is valid json
    try:
        payload = json.loads(obj)
    except:
        print "bad json"
        return None 
    #return an object packed with all the json stuff
    return Update(payload['userID'], payload['username'])
     

class EchoServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print('WebSocket connection request: {}'.format(request))

    def onMessage(self, payload, isBinary):
        update = object_decoder(payload)
        print payload
        self.sendMessage(payload, isBinary)
        print update.username


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        log.startLogging(sys.stdout)
        debug = True
    else:
        debug = False

    factory = WebSocketServerFactory(u'ws://127.0.0.1:8080',
                                     debug=debug,
                                     debugCodePaths=debug)
    factory.protocol = EchoServerProtocol

    resource = WebSocketResource(factory)

    root = File('.')

    root.putChild(u'ws', resource)

    site = Site(root)
    reactor.listenTCP(8080, site)

    reactor.run()
