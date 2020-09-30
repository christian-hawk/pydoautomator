Feature: Automate droplet creation
    '''As a tester/developer
    I want to automate floating ip assignment to droplet
    So I can automate my test pipeline'''

    Scenario Outline: Assign floating ip to droplet
        Given a droplet with id <droplet_id> exists
        And a floating ip with id <floating_ip> exists
        When assign_floating_ip_to_droplet is called
        Then floating ip should be assigned to droplet

        Examples:

            | droplet_id | floating_ip   |
            | 209808688  | 164.90.252.72 |
            | 209808839  | 167.172.15.77 |


