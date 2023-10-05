# Snowflake Adhoc Update

This sql script allows users to perform adhoc updates on the Snowflake production environment following a specific process. Here are the steps:

1. **Insert SQL Code**: Open the `click_data_ops/adhoc_task/snowflake_adhoc_script.sql` file and insert your SQL code. If there's any existing code in the file, remove it and add your code.

2. **Push to GitHub**: Commit your changes to a branch and push them to the remote repository.

3. **Create a Pull Request**: Create a pull request (PR) from your branch into the `master` branch. In the PR, describe your changes and request a review from a colleague.

4. **Review and Approval**: A colleague should review your PR. If everything looks good, they will approve it.

5. **Merging and Automation**: Once your PR is approved and merged into the `master` branch, GitHub Actions will automatically trigger. The workflow will execute the SQL code in `click_data_ops/adhoc_task/snowflake_adhoc_script.sql` on the Snowflake production environment.

Please follow this process carefully to ensure that your adhoc updates are applied correctly to the Snowflake production environment. For any questions or issues, please contact the repository maintainers.
