| Name                   | AccuKnox Container Scan                        |
|------------------------|-------------------------------------------------|
| Description            | Scan Docker images using AccuKnox and push the results to the CSPM panel. |
| Inputs                 |                                                   |
| dockerfile_context     | The context of the Dockerfile to use for building the image. (Required) |
| endpoint               | The URL of the CSPM panel to push the scan results to. (Required, default: `cspm.demo.accuknox.com`) |
| token                  | The token for authenticating with the CSPM panel. (Required) |
| tenant_id              | The ID of the tenant associated with the CSPM panel. (Required) |
| repository_name        | Docker image repository name. (Required) |
| tag                    | Add version tag to the repository. (Required, default: `${{ github.run_id }}`) |
| severity               | Allows selection of severity level for the scan. Options include UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL. If specified, the scan will target vulnerabilities of the selected severity level. (Optional, default: UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL) |
| code                   | Values '0' and '1' are accepted. '0' is the default value, which indicates that the pipeline will not be halted if the specified severity is found, while '1' indicates that the pipeline will stop if a specified severity level is detected. (Optional, default: 0) |   


| Name                   | AccuKnox Container Scan                        |
|------------------------|-------------------------------------------------|
| Description            | Scan Docker images using AccuKnox and push the results to the CSPM panel. |
| Inputs                 |                                                   |
| dockerfile_context     | The context of the Dockerfile to use for building the image. (Required) |
| endpoint               | The URL of the CSPM panel to push the scan results to. (Required, default: `cspm.demo.accuknox.com`) |
| token                  | The token for authenticating with the CSPM panel. (Required) |
| tenant_id              | The ID of the tenant associated with the CSPM panel. (Required) |
| repository_name        | Docker image repository name. (Required) |
| tag                    | Add version tag to the repository. (Required, default: `${{ github.run_id }}`) |
| Default Values         |                                                   |
| severity               | UNKNOWN, LOW, MEDIUM, HIGH, CRITICAL |
| code                   | 0 |
