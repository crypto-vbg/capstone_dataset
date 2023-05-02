import csv
import requests

# Set up authentication
headers = {'Authorization': 'Bearer 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'}

# Search for repositories related to Machine Learning
query = 'App+Development'
url = f'https://api.github.com/search/repositories?q={query}&per_page=100'
response = requests.get(url, headers=headers)
repositories = response.json()['items']

# Create a list to store the results
results = []

# Iterate over the repositories
for repo in repositories:
    repo_name = repo['name']
    repo_url = repo['html_url']
    repo_stars = repo['stargazers_count']
    repo_forks = repo['forks_count']
    repo_contributors_url = repo['contributors_url']
    
    # Retrieve the contributors information
    response = requests.get(repo_contributors_url, headers=headers)
    contributors = response.json()
    
    # Create a new row for each contributor and their contributions
    for contributor in contributors:
        contributor_name = contributor['login']
        contributor_contributions = contributor['contributions']
        results.append([repo_name, repo_url, repo_stars, repo_forks, contributor_name, contributor_contributions])

    # Check if there are more than 100 contributors
    while 'next' in response.links.keys():
        response = requests.get(response.links['next']['url'], headers=headers)
        contributors = response.json()
        
        # Create a new row for each contributor and their contributions
        for contributor in contributors:
            contributor_name = contributor['login']
            contributor_contributions = contributor['contributions']
            results.append([repo_name, repo_url, repo_stars, repo_forks, contributor_name, contributor_contributions])

# Create a CSV file with the results
with open('results_retrival_AppDev.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Repository Name', 'Repository URL', 'Stars', 'Forks', 'Contributor Name', 'Contributions'])
    writer.writerows(results)
