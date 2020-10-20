Feature: Automate droplet destruction
    '''As a tester/developer
    I want to destroy droplet
    So I can automate my test pipeline or save money'''

    Scenario Outline: Droplet destroy
        Given droplet <droplet_id> exists
        When destroy droplet is called
        Then droplet should be destroyed

        Examples:
            | droplet_id |
            | 213005489  |