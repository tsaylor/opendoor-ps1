import common, odSettings

class Reciprocity(common.BasePlugin):
    def authenticate(self, jCard):
        return True
        
    def authorize(self, jCard, resource):
        '''
        Compare a user's resource value to the threshold value and return boolean
        '''
        rules = self._get_rules()
        thresholds = odSettings.thresholds
        if rules.has_key(jCard.card['url']):
            rules = rules[jCard.card['url']]
            thresholds.update(rules['thresholds'])
            if jCard.card.get(resource.name, -1) >= thresholds.get(resource.name, 0):
                return True
        return False
        

    def _get_rules(self):
        '''
        if the rules dict contains the space's url as a key, it's on the whitelist.  If it has any threshold rules, those override the defaults for this space.
        '''
        rules = {
                'i3detroit.com':
                    {'thresholds':
                        {'memlevel':50,
                         'door':50,
                         'table saw':35
                        }
                    },
                'linuxleague.org':
                    {'thresholds':
                        {'linux':99
                        }
                    },
                'milwaukeemakerspace.com':None,
                }
                
