

| Name                | Description                                                                                           | Optional/Required | Default Values             |
|---------------------|-------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|
| dockerfile_context  | The context of the Dockerfile to use for building the image.                                           | Required          | -                           |
| endpoint            | The URL of the CSPM panel to push the scan results to.                                                 | Required          | `cspm.demo.accuknox.com`   |
| token               | The token for authenticating with the CSPM panel.                                                      | Required          | -                           |
| tenant_id           | The ID of the tenant associated with the CSPM panel.                                                  | Required          | -                           |
| repository_name     | Docker image repository name.                                                                        | Required          | -                           |
| tag                 | Add version tag to the repository.                                                                    | Required          | `${{ github.run_id }}`     |
| severity            | Allows selection of severity level for the scan. Options include UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL. | Optional          | `UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL` |
| code                | Specifies pipeline behavior upon detecting specified severity level. '0' (continue) or '1' (halt).    | Optional          | 0                           |
