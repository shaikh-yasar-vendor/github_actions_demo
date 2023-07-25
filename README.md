# Executing Snowflake SQL Command using GitHub Actions

This GitHub repository demonstrates how to run Snowflake SQL commands using GitHub Actions.

## Features

- Execute Snowflake SQL commands automatically when code is pushed from `my_branch_2` (this can be changed to any branch).
- Showcase the usage of SnowSQL, the Snowflake command-line client.
- Provide an example SQL script that interacts with Snowflake.

## Getting Started

### Prerequisites

- A Snowflake account with appropriate permissions to execute SQL commands. Place those in github secrets.

### How to Use

1. Clone this repository to your local machine:
2. git clone https://github.com/shaikh-yasar-vendor/github_actions_demo
3. Open the `snowflake_script.sql` file located in the home directory and make any necessary changes to the SQL script.
4. Commit your changes to the `my_branch_2` branch.
5. GitHub Actions will automatically trigger when you push to the `my_branch_2` branch, executing the SQL commands defined in the `snowflake_script.sql` file using SnowSQL.

## Directory Structure

- snowflake_script.sql: Contains the SQL script files to be executed.
- .github/workflows: Contains the GitHub Actions YAML file (e.g., `trigger.yaml`) responsible for running the SQL scripts using SnowSQL.

## GitHub Actions YAML File Explanation

The `trigger.yaml` GitHub Actions YAML file defines a workflow that runs the Snowflake SQL commands when code is pushed to the `my_branch_2` branch.

```yaml
name: Run Snowflake Script

# this will trigeer github action when code is pushed from my_branch_2 
on:
  push:
    branches:
      - my_branch_2
# jobs where actions will execute the task one by one
jobs:
  run_snowflake_script:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Download SnowSQL
        run:  curl -O https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowsql-1.2.27-linux_x86_64.bash
      - name: Install SnowSQL
        run: SNOWSQL_DEST=~ SNOWSQL_LOGIN_SHELL=~/.profile bash snowsql-1.2.27-linux_x86_64.bash
      - name: Test installation
        run:  ~/snowsql -v

      - name: Run Snowflake Script
        env:
          SNOWFLAKE_ACCOUNT: ${{ secrets.SNOWFLAKE_ACCOUNT }}
          SNOWFLAKE_USERNAME: ${{ secrets.SNOWFLAKE_USER }}
          SNOWSQL_PWD: ${{ secrets.SNOWSQL_PWD }}
          SNOWFLAKE_WAREHOUSE: ${{ secrets.SNOWFLAKE_WAREHOUSE }}
          SNOWFLAKE_DATABASE: ${{ secrets.SNOWFLAKE_DATABASE }}
          SNOWFLAKE_SCHEMA: ${{ secrets.SNOWFLAKE_SCHEMA }}
        run: |
          ~/snowsql -a $SNOWFLAKE_ACCOUNT -u $SNOWFLAKE_USERNAME -w $SNOWFLAKE_WAREHOUSE -d $SNOWFLAKE_DATABASE -s $SNOWFLAKE_SCHEMA -f snowflake_script.sql
```
The above YAMl file will execute the task step by step as defined.
1. It will use version 2 of github actions (which is new version)
2. Download the snowsql application into the ubuntu machine
3. Install the snowsql in Home directory
4. Test the snowsql is installed in the machine
5. execute the sql script by providing credentials which is stored in github actions
