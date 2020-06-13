# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure SQL database* |*basic compute gen5 & basic storage*|$4.99|
|*Azure Storage Account* | bandwidth & tables & tiered block blob| < $0.01
| *Azure App Service* | Free Tier| $0
| *Azure App Service Plan* | Basic Tier |  < $0.0.1

## Architecture Explanation
I chosed azure app service bacause it is a managed platform. This means that Azure takes care of application deployment and management, while the developer only needs to concentrate on app development. In addition to this, I did not full control over application management and deployment as in the case of VM

## Assess App changes

If the in the future, the application grow, and traffic increase, this will require me to design and configure the application and infrastructure to handle fluctuating traffic. VM will be my best option

## Link to Project
URL: http://flaskcms.azurewebsites.net/