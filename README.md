

| Input Values                | Description                                                                                           | Optional/Required | Default Values             |
|---------------------|-------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|
| dockerfile_context  | The context of the Dockerfile to use for building the image.                                           | Optional          | Dockerfile                           |
| endpoint            | The URL of the CSPM panel to push the scan results to.                                                 | Optional          | `cspm.demo.accuknox.com`   |
| token               | The token for authenticating with the CSPM panel.                                                      | Required          | -                           |
| tenant_id           | The ID of the tenant associated with the CSPM panel.                                                  | Required          | -                           |
| repository_name     | Docker image repository name.                                                                        | Required          | -                           |
| tag                 | Add version tag to the repository.                                                                    | Optional          | `${{ github.run_id }}`     |
| severity            | Allows selection of severity level for the scan. Options include UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL. | Optional          | `UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL` |
| code                | Specifies pipeline behavior upon detecting specified severity level. '0' (continue) or '1' (halt).    | Optional          | 0                           |


| Name              | Description                                                                                                                         | Optional/Required | Default Values                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------------|
| file              | File with infrastructure code or packages to scan                                                                                   | Optional          | -                                 |
| directory         | Directory with infrastructure code and/or package manager files to scan                                                             | Optional          | `.`                               |
| compact           | Do not display code blocks in output                                                                                                 | Optional          | -                                 |
| quiet             | Display only failed checks                                                                                                          | Optional          | -                                 |
| output_format     | The format of the output. Options: cli, json, junitxml, github_failed_only, or sarif (comma-separated)                              | Optional          | `json`                            |
| output_file_path  | Path and name for the output file, needs to end with a comma for a single output format                                             | Optional          | -                                 |
| soft_fail         | Do not return an error code if there are failed checks                                                                              | Optional          | -                                 |
| framework         | Run only on a specific infrastructure                                                                                                | Optional          | -                                 |
| skip_framework    | Skip a specific infrastructure                                                                                                      | Optional          | -                                 |
| github_pat        | Environment variable name for a Github personal access token for scanning external modules sourced from private repositories        | Optional          | -                                 |
| token             | The token for authenticating with the CSPM panel                                                                                     | Required          | -                                 |
| tenant_id         | The ID of the tenant associated with the CSPM panel                                                                                 | Required          | -                                 |
| endpoint          | The URL of the CSPM panel to push the scan results to                                                                               | Required          | `cspm.demo.accuknox.com`         |
