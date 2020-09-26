Feature: Automate droplet creation
    '''As a tester/developer
    I want to automate snapshot creation
    So I can automate my test pipeline'''

    Scenario Outline: Create droplet from snapshot
        Given snapshot name is <snapshot>
        And snapshot exists
        And host name is <host>
        When I receive a droplet start call
        Then droplet should be created
        And droplet name should be <host>

        Examples: gluu droplets

            | snapshot                        | host              |
            | t1.techno24x7.com-final-test420 | t1.techno24x7.com |
            | t1.techno24x7.com-latest-dev    | t1.techno24x7.com |

