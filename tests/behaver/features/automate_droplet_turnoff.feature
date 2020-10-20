Feature: Automate droplet turnoff
    '''As a tester/developer
    I want to turn off droplet
    So I can automate my test pipeline'''

    Scenario Outline: Droplet turnoff
        Given droplet <droplet_id> exists
        When turnoff droplet is called
        Then turnoff droplet

        Examples:
            | droplet_id |
            | 212611563  |