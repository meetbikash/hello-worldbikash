# Write-up Template


### Analyze, choose, and justify the appropriate resource option for deploying the app.



*For **both** a VM or App Service solution for the CMS app:
*
- *Analyze costs, scalability, availability, and workflow: following are some points for cost,scalability  and availability.
-Operational cost management like Tagging, Right size provisioned SKUs, Auto shutdown for VM,Cleanup orphan disk,compute cost, azure calculator, Adjust autoscale parameters,Horizontal over vertical scale autoscale when you select a VM within a series, we can only scale the VM up and down within that series, high availability for VMs and APPs etc
*
- *Choose the appropriate solution (VM or App Service) for deploying the app
App services for front websites with AD integration.
*
- *Justify your choice
Azure offers a number of ways to host application code. compute refers to the hosting model for the computing resources that your application runs on.

If an application consists of multiple workloads, evaluate each workload separately. A complete solution may incorporate two or more compute services.
for Ex:If i need a web front end with background processing and database backend to run business applications integrated with on premise assets,Azure App Service is a great solution for complex business applications. It lets us to develop apps that scale automatically on a load balanced platform, are secured with Active Directory, and connect to your on-premises resources. It makes managing those apps easy through a world-class portal and APIs, and allows us to gain insight into how customers are using them with app insight tools. The Webjobs feature lets us run background processes and tasks as part of ourr web tier, while hybrid connectivity and VNET features make it easy to connect back to on-premises resources. Azure App Service provides three 9's SLA for web apps and enables us to:

Run your applications reliably on a self-healing, auto-patching cloud platform.
Scale automatically across a global network of datacenters.
Back up and restore for disaster recovery.
Be ISO, SOC2, and PCI compliant.
Integrate with Active Directory

*

### Assess app changes that would change your decision.

Azure App Service makes it easy to avoid the infrastructure costs associated with migrating older IIS6 applications. Microsoft has created easy to use migration tools and detailed migration guidance that enable you to check compatibility and identify any changes that need to be made. Integration with Visual Studio, TFS, and common CMS tools makes it easy to deploy IIS6 applications directly to the cloud. Once deployed, the Azur Portal provides robust management tools that enable you to scale down to manage costs and up to meet demand as necessary. With the migration tool you can:

Quickly and easily migrate your legacy Windows Server 2003 web application to the cloud.
Opt to leave your attached SQL database on-premise to create a hybrid application.
Automatically move your SQL database along with your legacy application.



*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
When we decide to host a web application in the Azure cloud, the opportunity to explore the resources offered by a leading public cloud provider was exciting. How would Microsoft – with their deep experience and mature ecosystem – handle features like high availability, smart load balancing, and auto scaling?
It turns out that just choosing the right hosting service from Azure’s rich collection can be something of a challenge.
So, following the helpful Azure documentation, I successfully deployed my app using the App Service. Things went very smoothly… until I wanted to verify my server configurations and analyze some performance issues. It seems this isn’t possible, since App Service is a managed platform that handles deployment for you. There is no simple way to gain access to the app configuration files once it’s running.
In my case, this wasn’t ideal. I need remote access to the underlying web server, so that I can personally configure server tasks.
Azure App Servie, Azuru Cloud Service  and Virtual Machines are the three services that Microsoft Azure provides.
