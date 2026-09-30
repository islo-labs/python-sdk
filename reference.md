# Reference
## byo
<details><summary><code>client.byo.<a href="src/islo/byo/client.py">start_byo_inference_setup</a>(...) -> ByoSetupResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, ByoSourceKind
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.byo.start_byo_inference_setup(
    source_kind=ByoSourceKind.DATABRICKS,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source_kind:** `ByoSourceKind` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.byo.<a href="src/islo/byo/client.py">get_byo_inference_status</a>() -> ByoStatusResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.byo.get_byo_inference_status()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CloudRoles
<details><summary><code>client.cloud_roles.<a href="src/islo/cloud_roles/client.py">list_cloud_roles</a>(...) -> ListPageCloudRoleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.cloud_roles.list_cloud_roles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[CloudRoleType]` — Filter by role type
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_roles.<a href="src/islo/cloud_roles/client.py">create_cloud_role</a>(...) -> CloudRoleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, CloudProvider
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.cloud_roles.create_cloud_role(
    provider=CloudProvider.AWS,
    role_arn="role_arn",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `CloudProvider` 
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_duration_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[CloudRoleType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_roles.<a href="src/islo/cloud_roles/client.py">get_cloud_role</a>(...) -> CloudRoleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.cloud_roles.get_cloud_role(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_roles.<a href="src/islo/cloud_roles/client.py">delete_cloud_role</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.cloud_roles.delete_cloud_role(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cloud_roles.<a href="src/islo/cloud_roles/client.py">update_cloud_role</a>(...) -> CloudRoleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.cloud_roles.update_cloud_role(
    role_id="role_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**session_duration_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ComputeEvents
<details><summary><code>client.compute_events.<a href="src/islo/compute_events/client.py">get_compute_event</a>(...) -> ComputeEventDetailResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.compute_events.get_compute_event(
    command_id="command_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**command_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ContainerRegistries
<details><summary><code>client.container_registries.<a href="src/islo/container_registries/client.py">list_container_registries</a>() -> ListPageContainerRegistryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.container_registries.list_container_registries()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.container_registries.<a href="src/islo/container_registries/client.py">create_container_registry</a>(...) -> ContainerRegistryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, RegistryProvider
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.container_registries.create_container_registry(
    cloud_role_id="cloud_role_id",
    provider=RegistryProvider.ECR,
    region="region",
    registry_host="registry_host",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cloud_role_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `RegistryProvider` 
    
</dd>
</dl>

<dl>
<dd>

**region:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**registry_host:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**repository_prefixes:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.container_registries.<a href="src/islo/container_registries/client.py">get_container_registry</a>(...) -> ContainerRegistryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.container_registries.get_container_registry(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.container_registries.<a href="src/islo/container_registries/client.py">delete_container_registry</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.container_registries.delete_container_registry(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.container_registries.<a href="src/islo/container_registries/client.py">update_container_registry</a>(...) -> ContainerRegistryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.container_registries.update_container_registry(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cloud_role_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**repository_prefixes:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credits
<details><summary><code>client.credits.<a href="src/islo/credits/client.py">get_credit_balance</a>() -> CreditBalance</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the tenant's available prepaid credit balance in cents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.credits.get_credit_balance()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Environments
<details><summary><code>client.environments.<a href="src/islo/environments/client.py">list_environments</a>(...) -> ListPageEnvironmentListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.list_environments()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/islo/environments/client.py">create_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.create_environment(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Optional[typing.List[EnvironmentCreateEntriesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/islo/environments/client.py">get_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.get_environment(
    environment_ref="environment_ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/islo/environments/client.py">delete_environment</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.delete_environment(
    environment_ref="environment_ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/islo/environments/client.py">update_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.update_environment(
    environment_ref="environment_ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**entries:** `typing.Optional[typing.List[EnvironmentUpdateEntriesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/islo/environments/client.py">set_default_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.set_default_environment(
    environment_ref="environment_ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.environments.<a href="src/islo/environments/client.py">unset_default_environment</a>(...) -> EnvironmentResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.environments.unset_default_environment(
    environment_ref="environment_ref",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**environment_ref:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Factories
<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factories</a>() -> ListPageFactoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factories()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">create_factory</a>(...) -> FactoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.create_factory(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factories_overview</a>() -> FactoryOverview</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factories_overview()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory</a>(...) -> FactoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">update_factory</a>(...) -> FactoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.update_factory(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**icon:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[FactoryStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">activate_factory</a>(...) -> FactoryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.activate_factory(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_agent_sessions</a>(...) -> ListPageAgentSessionListItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_agent_sessions(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**include_subagents:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_agent_session</a>(...) -> AgentSessionListItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_agent_session(
    factory_id="factory_id",
    session_name="session_name",
    sandbox_id="sandbox_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_agent_session_events</a>(...) -> ListPageAgentSessionEventResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_agent_session_events(
    factory_id="factory_id",
    session_name="session_name",
    sandbox_id="sandbox_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_path:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include_descendants:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_agent_turn</a>(...) -> FactoryAgentTurnResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_agent_turn(
    factory_id="factory_id",
    turn_id="turn_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**turn_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_job_runs</a>(...) -> ListPageJobRunListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_job_runs(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_job_run_facets</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_job_run_facets(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_job_run_by_id</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_job_run_by_id(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_resource_jobs</a>(...) -> ListPageJobListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_resource_jobs(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_job</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_job(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">delete_scoped_factory_job</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.delete_scoped_factory_job(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">deploy_scoped_factory_job</a>(...) -> JobVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, JobManifestInput, JobSection, RunSectionInput, TaskInput, TaskStepInput
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.deploy_scoped_factory_job(
    factory_id="factory_id",
    name="name",
    manifest=JobManifestInput(
        job=JobSection(
            name="name",
        ),
        run=RunSectionInput(
            tasks=[
                TaskInput(
                    name="name",
                    steps=[
                        TaskStepInput()
                    ],
                )
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_scoped_factory_job_runs</a>(...) -> ListPageJobRunListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_scoped_factory_job_runs(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">trigger_scoped_factory_job_run</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.trigger_scoped_factory_job_run(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobRunCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_job_run</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_job_run(
    factory_id="factory_id",
    name="name",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">stop_scoped_factory_job_run</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.stop_scoped_factory_job_run(
    factory_id="factory_id",
    name="name",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobRunStopRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_job_schedule</a>(...) -> JobScheduleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_job_schedule(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">delete_scoped_factory_job_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.delete_scoped_factory_job_schedule(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">validate_scoped_factory_job_manifest</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, JobManifestInput, JobSection, RunSectionInput, TaskInput, TaskStepInput
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.validate_scoped_factory_job_manifest(
    factory_id="factory_id",
    name="name",
    manifest=JobManifestInput(
        job=JobSection(
            name="name",
        ),
        run=RunSectionInput(
            tasks=[
                TaskInput(
                    name="name",
                    steps=[
                        TaskStepInput()
                    ],
                )
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_scoped_factory_job_versions</a>(...) -> ListPageJobVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_scoped_factory_job_versions(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_job_version</a>(...) -> JobVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_job_version(
    factory_id="factory_id",
    name="name",
    version_id="version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_knowledge</a>(...) -> ListPageKnowledgeItemListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_knowledge(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[KnowledgeLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[KnowledgeLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**repository:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFactoryKnowledgeRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">create_factory_knowledge</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.create_factory_knowledge(
    factory_id="factory_id",
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `KnowledgeItemCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_knowledge_facets</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_knowledge_facets(
    factory_id="factory_id",
    fields=[
        "fields"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_knowledge_tags</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_knowledge_tags(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">create_factory_knowledge_media</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.create_factory_knowledge_media(
    factory_id="factory_id",
    file="example_file",
    item="item",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Media file
    
</dd>
</dl>

<dl>
<dd>

**item:** `str` — JSON metadata for the knowledge item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_knowledge</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_knowledge(
    factory_id="factory_id",
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">delete_factory_knowledge</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.delete_factory_knowledge(
    factory_id="factory_id",
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">update_factory_knowledge</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.update_factory_knowledge(
    factory_id="factory_id",
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KnowledgeItemUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_knowledge_content</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_knowledge_content(
    factory_id="factory_id",
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">put_factory_knowledge_content</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.put_factory_knowledge_content(
    factory_id="factory_id",
    identifier="identifier",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Replacement content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">restore_factory_knowledge_version</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.restore_factory_knowledge_version(
    factory_id="factory_id",
    identifier="identifier",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KnowledgeRestoreRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_knowledge_versions</a>(...) -> ListPageKnowledgeVersionListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_knowledge_versions(
    factory_id="factory_id",
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListFactoryKnowledgeVersionsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_knowledge_version</a>(...) -> KnowledgeVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_knowledge_version(
    factory_id="factory_id",
    identifier="identifier",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_factory_knowledge_version_content</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_factory_knowledge_version_content(
    factory_id="factory_id",
    identifier="identifier",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_line_runs_across_lines</a>(...) -> ListPageLineRunSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_line_runs_across_lines(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**line_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_resource_line_run_facets</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_resource_line_run_facets(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**line_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_line_run(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">ask_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.ask_scoped_factory_line_run(
    factory_id="factory_id",
    run_id="run_id",
    message="message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunAskRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">cancel_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.cancel_scoped_factory_line_run(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunControlRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_line_run_debug</a>(...) -> LineRunDebugResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_line_run_debug(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_scoped_factory_line_run_events</a>(...) -> ListPageLineEventResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_scoped_factory_line_run_events(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">retry_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.retry_scoped_factory_line_run(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">steer_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.steer_scoped_factory_line_run(
    factory_id="factory_id",
    run_id="run_id",
    stage_name="stage_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunSteerRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">stop_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.stop_scoped_factory_line_run(
    factory_id="factory_id",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunControlRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_factory_resource_lines</a>(...) -> ListPageLineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_factory_resource_lines(
    factory_id="factory_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_line</a>(...) -> LineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_line(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">delete_scoped_factory_line</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.delete_scoped_factory_line(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">update_scoped_factory_line</a>(...) -> LineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.update_scoped_factory_line(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">deploy_scoped_factory_line</a>(...) -> LineVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, LineManifestInput, LineSection, LineStage, LineManifestInputTrigger_IntegrationTrigger, IntegrationTriggerSectionInputSelector_Github
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.deploy_scoped_factory_line(
    factory_id="factory_id",
    name="name",
    manifest=LineManifestInput(
        line=LineSection(
            name="name",
        ),
        stages=[
            LineStage(
                id="id",
                job="job",
            )
        ],
        trigger=LineManifestInputTrigger_IntegrationTrigger(
            name="name",
            provider="provider",
            selector=IntegrationTriggerSectionInputSelector_Github(),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_scoped_factory_line_runs</a>(...) -> ListPageLineRunSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_scoped_factory_line_runs(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">trigger_scoped_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.trigger_scoped_factory_line_run(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">get_scoped_factory_line_schedule</a>(...) -> LineScheduleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.get_scoped_factory_line_schedule(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">upsert_scoped_factory_line_schedule</a>(...) -> LineScheduleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.upsert_scoped_factory_line_schedule(
    factory_id="factory_id",
    name="name",
    cron="cron",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineScheduleUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">delete_scoped_factory_line_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.delete_scoped_factory_line_schedule(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">validate_scoped_factory_line_manifest</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, LineManifestInput, LineSection, LineStage, LineManifestInputTrigger_IntegrationTrigger, IntegrationTriggerSectionInputSelector_Github
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.validate_scoped_factory_line_manifest(
    factory_id="factory_id",
    name="name",
    manifest=LineManifestInput(
        line=LineSection(
            name="name",
        ),
        stages=[
            LineStage(
                id="id",
                job="job",
            )
        ],
        trigger=LineManifestInputTrigger_IntegrationTrigger(
            name="name",
            provider="provider",
            selector=IntegrationTriggerSectionInputSelector_Github(),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factories.<a href="src/islo/factories/client.py">list_scoped_factory_line_versions</a>(...) -> ListPageLineVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factories.list_scoped_factory_line_versions(
    factory_id="factory_id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Machines
<details><summary><code>client.machines.<a href="src/islo/machines/client.py">list_factory_machines</a>(...) -> ListPageMachineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.machines.list_factory_machines(
    factory="factory",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.machines.<a href="src/islo/machines/client.py">create_factory_machine</a>(...) -> MachineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.machines.create_factory_machine(
    factory="factory",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.List[MachineCreateCapabilitiesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**disk_gb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gateway_profile:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lifecycle:** `typing.Optional[LifecyclePolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**repos:** `typing.Optional[typing.List[ControlPlaneGitSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[MachineSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**vcpus:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.machines.<a href="src/islo/machines/client.py">get_factory_machine</a>(...) -> MachineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.machines.get_factory_machine(
    factory="factory",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.machines.<a href="src/islo/machines/client.py">delete_factory_machine</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.machines.delete_factory_machine(
    factory="factory",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.machines.<a href="src/islo/machines/client.py">update_factory_machine</a>(...) -> MachineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.machines.update_factory_machine(
    factory="factory",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.List[MachineUpdateCapabilitiesItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**disk_gb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gateway_profile:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**lifecycle:** `typing.Optional[LifecyclePolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**repos:** `typing.Optional[typing.List[ControlPlaneGitSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**schedule:** `typing.Optional[MachineSchedule]` 
    
</dd>
</dl>

<dl>
<dd>

**vcpus:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.machines.<a href="src/islo/machines/client.py">build_factory_machine</a>(...) -> MachineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.machines.build_factory_machine(
    factory="factory",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factory:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## factory
<details><summary><code>client.factory.<a href="src/islo/factory/client.py">list_factory_line_runs</a>(...) -> ListPageLineRunSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.list_factory_line_runs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort order. Allowed: -created_at, created_at
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**line_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">list_factory_line_run_facets</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.list_factory_line_run_facets(
    fields=[
        "fields"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Facet fields to return (e.g. line_name, status)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**line_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">get_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.get_factory_line_run(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">ask_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.ask_factory_line_run(
    run_id="run_id",
    message="message",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunAskRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">cancel_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.cancel_factory_line_run(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunControlRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">get_factory_line_run_debug</a>(...) -> LineRunDebugResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Per-stage and per-step diagnostics for one line run, including the last failed stage attempt's first failing step, each step's exit code and output tails, and the sandbox environment each stage ran in.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.get_factory_line_run_debug(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">list_factory_line_run_events</a>(...) -> ListPageLineEventResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.list_factory_line_run_events(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**event_types:** `typing.Optional[typing.List[str]]` — Restrict the timeline to these event types
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">retry_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.retry_factory_line_run(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">steer_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.steer_factory_line_run(
    run_id="run_id",
    stage_name="stage_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunSteerRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">stop_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.stop_factory_line_run(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunControlRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">list_factory_lines</a>(...) -> ListPageLineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.list_factory_lines()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">get_factory_line</a>(...) -> LineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.get_factory_line(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">delete_factory_line</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.delete_factory_line(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">update_factory_line</a>(...) -> LineResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.update_factory_line(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">deploy_factory_line</a>(...) -> LineVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, LineManifestInput, LineSection, LineStage, LineManifestInputTrigger_IntegrationTrigger, IntegrationTriggerSectionInputSelector_Github
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.deploy_factory_line(
    name="name",
    manifest=LineManifestInput(
        line=LineSection(
            name="name",
        ),
        stages=[
            LineStage(
                id="id",
                job="job",
            )
        ],
        trigger=LineManifestInputTrigger_IntegrationTrigger(
            name="name",
            provider="provider",
            selector=IntegrationTriggerSectionInputSelector_Github(),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">list_factory_line_runs_for_line</a>(...) -> ListPageLineRunSummary</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.list_factory_line_runs_for_line(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">trigger_factory_line_run</a>(...) -> LineRunDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.trigger_factory_line_run(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineRunCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">get_factory_line_schedule</a>(...) -> LineScheduleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.get_factory_line_schedule(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">upsert_factory_line_schedule</a>(...) -> LineScheduleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.upsert_factory_line_schedule(
    name="name",
    cron="cron",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineScheduleUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">delete_factory_line_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.delete_factory_line_schedule(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">validate_factory_line_manifest</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, LineManifestInput, LineSection, LineStage, LineManifestInputTrigger_IntegrationTrigger, IntegrationTriggerSectionInputSelector_Github
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.validate_factory_line_manifest(
    name="name",
    manifest=LineManifestInput(
        line=LineSection(
            name="name",
        ),
        stages=[
            LineStage(
                id="id",
                job="job",
            )
        ],
        trigger=LineManifestInputTrigger_IntegrationTrigger(
            name="name",
            provider="provider",
            selector=IntegrationTriggerSectionInputSelector_Github(),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `LineDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.factory.<a href="src/islo/factory/client.py">list_factory_line_versions</a>(...) -> ListPageLineVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.factory.list_factory_line_versions(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## gateway-profiles
<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">list_gateway_profiles</a>() -> ListPageGatewayProfileResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.list_gateway_profiles()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">create_gateway_profile</a>(...) -> GatewayProfileResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.create_gateway_profile(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cloud_role:** `typing.Optional[str]` — Cloud role public ID (UUID)
    
</dd>
</dl>

<dl>
<dd>

**default_action:** `typing.Optional[GatewayAction]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_policy:** `typing.Optional[GatewayProfileCreateIntegrationPolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**internet_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">get_gateway_profile</a>(...) -> GatewayProfileDetailResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.get_gateway_profile(
    profile_id="profile_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">delete_gateway_profile</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.delete_gateway_profile(
    profile_id="profile_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">update_gateway_profile</a>(...) -> GatewayProfileResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.update_gateway_profile(
    profile_id="profile_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cloud_role:** `typing.Optional[str]` — Cloud role public ID (UUID), empty string to unset
    
</dd>
</dl>

<dl>
<dd>

**default_action:** `typing.Optional[GatewayAction]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**integration_policy:** `typing.Optional[GatewayProfileUpdateIntegrationPolicy]` — Omit to leave unchanged; send {"mode": "all"} to allow all integrations
    
</dd>
</dl>

<dl>
<dd>

**internet_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">create_gateway_rule</a>(...) -> GatewayRuleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.create_gateway_rule(
    profile_id="profile_id",
    host_pattern="host_pattern",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**host_pattern:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[GatewayAction]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_strategy:** `typing.Optional[AuthStrategySchema]` 
    
</dd>
</dl>

<dl>
<dd>

**content_filter:** `typing.Optional[GatewayRuleCreateContentFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**methods:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**path_pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_rpm:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">reorder_gateway_rules</a>(...) -> typing.List[GatewayRuleResponse]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, RuleReorderItem
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.reorder_gateway_rules(
    profile_id="profile_id",
    rules=[
        RuleReorderItem(
            priority=1,
            rule_id="rule_id",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.List[RuleReorderItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">delete_gateway_rule</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.delete_gateway_rule(
    profile_id="profile_id",
    rule_id="rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rule_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">update_gateway_rule</a>(...) -> GatewayRuleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.update_gateway_rule(
    profile_id="profile_id",
    rule_id="rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**rule_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[GatewayAction]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_strategy:** `typing.Optional[AuthStrategySchema]` 
    
</dd>
</dl>

<dl>
<dd>

**content_filter:** `typing.Optional[GatewayRuleUpdateContentFilter]` 
    
</dd>
</dl>

<dl>
<dd>

**host_pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**methods:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**path_pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_rpm:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## inference
<details><summary><code>client.inference.<a href="src/islo/inference/client.py">list_inference_models</a>() -> InferenceModelsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.inference.list_inference_models()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## integrations
<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integrations</a>() -> ListPageIntegrationStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the integrations the user/tenant has connected.

Includes preset providers (from the PROVIDERS registry) and tenant-scoped
custom outbound apps (filtered out of Descope's load_all_applications).
Returns one entry per connected (provider, scope, auth_type) slot, so a
provider with both a personal api_key and a personal oauth token will
appear twice. Disconnected slots are not emitted; clients that need a
list of available-but-not-connected providers should call
``GET /integrations/providers`` instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.list_integrations()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_custom_services</a>() -> ListPageCustomService</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List custom service definitions in the current tenant (catalog view).

Returns every custom Descope app belonging to the tenant regardless of
connection status, so the Add Integration picker can surface them for
any tenant member to connect to. Connection state (per-user/per-workspace
tokens) lives on ``GET /integrations``; this endpoint is purely the
service catalog.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.list_custom_services()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">create_custom_service</a>(...) -> CustomServiceCreateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a tenant-scoped custom Descope outbound app.

Returns the ``app_id`` so the frontend can immediately kick off the
connect flow (OAuth) or surface the API key form. Presets do not pass
through this endpoint -- their app ids come straight from
``GET /integrations/providers``.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, CustomIntegration
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.create_custom_service(
    custom=CustomIntegration(
        name="name",
        slug="slug",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**custom:** `CustomIntegration` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">disconnect_custom_integration</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect a custom integration by its stable provider slug.

The provider is resolved only within the authenticated tenant's custom
service catalog, so callers cannot target another workspace. ``scope`` selects
which side's tokens to revoke (per-user vs tenant-wide);
``delete_app=true`` removes the Descope app entirely (affects every user in
the workspace).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.disconnect_custom_integration(
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[IntegrationLevel]` — Which token to revoke: 'user' (this user's personal) or 'tenant' (workspace)
    
</dd>
</dl>

<dl>
<dd>

**delete_app:** `typing.Optional[bool]` — Also remove the Descope outbound app entirely (affects every user in this workspace)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integration_providers</a>() -> ListPageIntegrationProvider</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the integration providers available to connect from Islo, including the supported authentication methods and connection scopes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.list_integration_providers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integration_trigger_events</a>(...) -> TriggerEventPage</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.list_integration_trigger_events()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListIntegrationTriggerEventsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**event_name:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**invocation_status:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**received_at:** `typing.Optional[TimestampRange]` — received_at range. Operators: gte, gt, lte, lt. Serialized as received_at[gte]=…&received_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">get_integration_trigger_event</a>(...) -> TriggerEventDetail</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.get_integration_trigger_event(
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**event_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integration_triggers</a>() -> ListPageTriggerCatalogItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.list_integration_triggers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_connected_integration_triggers</a>() -> ListPageTriggerCatalogItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.list_connected_integration_triggers()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">get_integration_trigger</a>(...) -> TriggerCatalogItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.get_integration_trigger(
    provider="provider",
    trigger_name="trigger_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**trigger_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">get_integration_status</a>(...) -> IntegrationDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the detailed status of a specific integration.

Returns both user-level and tenant-level connection status independently.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.get_integration_status(
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">disconnect_integration</a>(...) -> typing.Dict[str, typing.Any]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disconnect/revoke an integration.

Args:
    provider: Provider name
    level: Which level to disconnect (USER or TENANT)
    auth_type: Optional. Defaults to provider's primary type.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.disconnect_integration(
    provider="provider",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**level:** `typing.Optional[IntegrationLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**auth_type:** `typing.Optional[AuthMethod]` — oauth or api_key
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## JobRuns
<details><summary><code>client.job_runs.<a href="src/islo/job_runs/client.py">list_all_job_runs</a>(...) -> ListPageJobRunListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.job_runs.list_all_job_runs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort order. Allowed: -created_at, created_at
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job_runs.<a href="src/islo/job_runs/client.py">list_job_run_facets</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.job_runs.list_job_run_facets(
    fields=[
        "fields"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Facet fields to return (e.g. job_name, status)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**job_name:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[TimestampRange]` — created_at range. Operators: gte, gt, lte, lt. Serialized as created_at[gte]=…&created_at[lt]=…
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.job_runs.<a href="src/islo/job_runs/client.py">get_job_run_by_id</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.job_runs.get_job_run_by_id(
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## jobs
<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">list_jobs</a>(...) -> ListPageJobListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.list_jobs()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">get_job</a>(...) -> JobResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.get_job(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">delete_job</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.delete_job(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">deploy_job</a>(...) -> JobVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, JobManifestInput, JobSection, RunSectionInput, TaskInput, TaskStepInput
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.deploy_job(
    name="name",
    manifest=JobManifestInput(
        job=JobSection(
            name="name",
        ),
        run=RunSectionInput(
            tasks=[
                TaskInput(
                    name="name",
                    steps=[
                        TaskStepInput()
                    ],
                )
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">list_job_runs</a>(...) -> ListPageJobRunListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.list_job_runs(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">trigger_job_run</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.trigger_job_run(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobRunCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">get_job_run</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.get_job_run(
    name="name",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">stop_job_run</a>(...) -> JobRunResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.stop_job_run(
    name="name",
    run_id="run_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**run_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobRunStopRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">get_job_schedule</a>(...) -> JobScheduleResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.get_job_schedule(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">delete_job_schedule</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.delete_job_schedule(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">validate_job_manifest</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, JobManifestInput, JobSection, RunSectionInput, TaskInput, TaskStepInput
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.validate_job_manifest(
    name="name",
    manifest=JobManifestInput(
        job=JobSection(
            name="name",
        ),
        run=RunSectionInput(
            tasks=[
                TaskInput(
                    name="name",
                    steps=[
                        TaskStepInput()
                    ],
                )
            ],
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `JobDeployRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">list_job_versions</a>(...) -> ListPageJobVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.list_job_versions(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.jobs.<a href="src/islo/jobs/client.py">get_job_version</a>(...) -> JobVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.jobs.get_job_version(
    name="name",
    version_id="version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## knowledge
<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">list_knowledge</a>(...) -> ListPageKnowledgeItemListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.list_knowledge()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**level:** `typing.Optional[KnowledgeLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[KnowledgeLevel]` 
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**repository:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search identifier or body text
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListKnowledgeRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">create_knowledge</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.create_knowledge(
    slug="slug",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `KnowledgeItemCreate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">list_knowledge_facets</a>(...) -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.list_knowledge_facets(
    fields=[
        "fields"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fields:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">list_knowledge_tags</a>() -> FacetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.list_knowledge_tags()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">create_knowledge_media</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.create_knowledge_media(
    file="example_file",
    item="item",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `core.File` — Media file
    
</dd>
</dl>

<dl>
<dd>

**item:** `str` — JSON metadata for the knowledge item
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">get_knowledge</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.get_knowledge(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">delete_knowledge</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.delete_knowledge(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">update_knowledge</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.update_knowledge(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KnowledgeItemUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">get_knowledge_content</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.get_knowledge_content(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">put_knowledge_content</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.put_knowledge_content(
    identifier="identifier",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` — Replacement content
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">restore_knowledge_version</a>(...) -> KnowledgeItemResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.restore_knowledge_version(
    identifier="identifier",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**request:** `KnowledgeRestoreRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">list_knowledge_versions</a>(...) -> ListPageKnowledgeVersionListResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.list_knowledge_versions(
    identifier="identifier",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ListKnowledgeVersionsRequestSort]` 
    
</dd>
</dl>

<dl>
<dd>

**include:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">get_knowledge_version</a>(...) -> KnowledgeVersionResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.get_knowledge_version(
    identifier="identifier",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.knowledge.<a href="src/islo/knowledge/client.py">get_knowledge_version_content</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.knowledge.get_knowledge_version_content(
    identifier="identifier",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**identifier:** `str` — Unique lowercase identifier (letters, digits, hyphens). Set at creation and cannot be changed.
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SandboxTemplates
<details><summary><code>client.sandbox_templates.<a href="src/islo/sandbox_templates/client.py">list_sandbox_templates</a>(...) -> ListPageTemplateListItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandbox_templates.list_sandbox_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox_templates.<a href="src/islo/sandbox_templates/client.py">create_sandbox_template</a>(...) -> TemplateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandbox_templates.create_sandbox_template(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**disk_gb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gateway_profile_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**init:** `typing.Optional[TemplateCreateInit]` 
    
</dd>
</dl>

<dl>
<dd>

**lifecycle:** `typing.Optional[LifecyclePolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.List[ControlPlaneGitSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**vcpus:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox_templates.<a href="src/islo/sandbox_templates/client.py">get_sandbox_template</a>(...) -> TemplateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandbox_templates.get_sandbox_template(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox_templates.<a href="src/islo/sandbox_templates/client.py">delete_sandbox_template</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandbox_templates.delete_sandbox_template(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox_templates.<a href="src/islo/sandbox_templates/client.py">update_sandbox_template</a>(...) -> TemplateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandbox_templates.update_sandbox_template(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**disk_gb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**environment_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**gateway_profile_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**init:** `typing.Optional[TemplateUpdateInit]` 
    
</dd>
</dl>

<dl>
<dd>

**lifecycle:** `typing.Optional[LifecyclePolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.List[ControlPlaneGitSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**vcpus:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandbox_templates.<a href="src/islo/sandbox_templates/client.py">get_sandbox_template_version</a>(...) -> TemplateResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandbox_templates.get_sandbox_template_version(
    name="name",
    version_number=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version_number:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## tenants
<details><summary><code>client.tenants.<a href="src/islo/tenants/client.py">list_tenant_compute_regions</a>() -> ListPageComputeRegionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the compute regions the authenticated tenant may use, including the API and WebSocket base URLs for each region.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.tenants.list_tenant_compute_regions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## sandboxes
<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_sandboxes</a>(...) -> PaginatedSandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List sandboxes for the authenticated tenant with optional filters and pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.list_sandboxes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search term for sandbox name, image, creator, or public ID. Takes precedence over `search` when both are provided.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search term for sandbox name, image, creator, or public ID. Alias for `q`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name_prefix:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">create_sandbox</a>(...) -> SandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new sandbox VM with the requested resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.create_sandbox()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cache_key:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**disk_gb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**env:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**environment:** `typing.Optional[str]` — Environment for sandbox env and environment-owned gateway injection.
    
</dd>
</dl>

<dl>
<dd>

**gateway_profile:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**init:** `typing.Optional[SandboxInit]` 
    
</dd>
</dl>

<dl>
<dd>

**internet_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**lifecycle:** `typing.Optional[LifecyclePolicy]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**setup_scripts:** `typing.Optional[typing.List[SetupScript]]` 
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**sources:** `typing.Optional[typing.List[GitSource]]` 
    
</dd>
</dl>

<dl>
<dd>

**vcpus:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**workdir:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_sandbox_by_id</a>(...) -> SandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return details for a sandbox by public ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_sandbox_by_id(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Sandbox public ID (UUID)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_sandbox</a>(...) -> SandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return details for a sandbox by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_sandbox(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">delete_sandbox</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a sandbox and clean up its running VM, if any.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.delete_sandbox(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_creation_events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Server-sent events for live sandbox creation progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_creation_events(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">exec_in_sandbox</a>(...) -> ExecResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a command in a sandbox and return an exec ID for polling results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.exec_in_sandbox(
    sandbox_name="sandbox_name",
    command=[
        "command"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExecRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">exec_in_sandbox_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream command stdout, stderr, and exit events as Server-Sent Events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.exec_in_sandbox_stream(
    sandbox_name="sandbox_name",
    command=[
        "command"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request:** `ExecRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_exec_result</a>(...) -> ExecResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the captured result for a previously started sandbox command.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_exec_result(
    sandbox_name="sandbox_name",
    exec_id="exec_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` — Exec ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">download_file</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a file from a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.download_file(
    sandbox_name="sandbox_name",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — File path inside the sandbox
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">upload_file</a>(...) -> FileUploadStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a file to a path inside a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.upload_file(
    sandbox_name="sandbox_name",
    path="path",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Destination path inside the sandbox
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">download_archive</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a sandbox directory as an archive.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.download_archive(
    sandbox_name="sandbox_name",
    path="path",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Directory path to archive inside the sandbox
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">upload_archive</a>(...) -> FileUploadStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload and extract an archive into a sandbox directory.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.upload_archive(
    sandbox_name="sandbox_name",
    path="path",
    file="example_file",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Destination directory inside the sandbox
    
</dd>
</dl>

<dl>
<dd>

**file:** `core.File` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">pause_sandbox</a>(...) -> SandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pause a running sandbox VM.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.pause_sandbox(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">resume_sandbox</a>(...) -> SandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resume a paused sandbox VM.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.resume_sandbox(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_sessions</a>(...) -> ListSessionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List persistent shell sessions in a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.list_sessions(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">create_session</a>(...) -> CreateSessionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a persistent shell session in a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.create_session(
    sandbox_name="sandbox_name",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**command:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**env:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 
    
</dd>
</dl>

<dl>
<dd>

**ttl:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**workdir:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">kill_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate a persistent shell session in a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.kill_session(
    sandbox_name="sandbox_name",
    session="session",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**session:** `str` — Session name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">stop_sandbox</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop the sandbox VM while keeping the sandbox record available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.stop_sandbox(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## shares
<details><summary><code>client.shares.<a href="src/islo/shares/client.py">list_shares</a>(...) -> typing.List[ShareResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active public shares for a sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.shares.list_shares(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/islo/shares/client.py">create_share</a>(...) -> ShareResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a temporary public share for a sandbox port.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.shares.create_share(
    sandbox_name="sandbox_name",
    port=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**ttl_seconds:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.shares.<a href="src/islo/shares/client.py">revoke_share</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke a sandbox port share.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.shares.revoke_share(
    sandbox_name="sandbox_name",
    share_id="share_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**share_id:** `str` — Share ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## snapshots
<details><summary><code>client.snapshots.<a href="src/islo/snapshots/client.py">list_snapshots</a>(...) -> PaginatedSnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all snapshots for the current tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.snapshots.list_snapshots()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/islo/snapshots/client.py">create_snapshot</a>(...) -> SnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a snapshot from a running sandbox. By default, waits for capture and returns a ready snapshot. Send `Prefer: respond-async` to return immediately with a saving snapshot.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.snapshots.create_snapshot(
    sandbox_name="sandbox_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/islo/snapshots/client.py">get_snapshot</a>(...) -> SnapshotResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get snapshot details by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.snapshots.get_snapshot(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Snapshot name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.snapshots.<a href="src/islo/snapshots/client.py">delete_snapshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a snapshot by name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.snapshots.delete_snapshot(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Snapshot name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## webhooks
<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">list_incoming_webhooks</a>() -> typing.List[IncomingWebhook]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active incoming webhooks for the tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.list_incoming_webhooks()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">create_incoming_webhook</a>(...) -> IncomingWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a tenant-scoped incoming webhook receiver. The receiver URL accepts external webhook deliveries and routes them to a resolved sandbox.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo, IncomingWebhookAuthZero, IncomingWebhookAuthZeroAuthType, IdempotencyConfig_Header, IncomingWebhookTarget_FixedSandboxName
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.create_incoming_webhook(
    auth=IncomingWebhookAuthZero(
        auth_type=IncomingWebhookAuthZeroAuthType.NONE,
    ),
    idempotency=IdempotencyConfig_Header(
        name="name",
    ),
    name="name",
    target=IncomingWebhookTarget_FixedSandboxName(
        sandbox_name="sandbox_name",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth:** `IncomingWebhookAuth` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency:** `IdempotencyConfig` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `IncomingWebhookTarget` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.Optional[typing.List[IncomingWebhookRule]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IncomingWebhookStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">get_incoming_webhook</a>(...) -> IncomingWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get one incoming webhook by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.get_incoming_webhook(
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Incoming webhook ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">delete_incoming_webhook</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete an incoming webhook receiver.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.delete_incoming_webhook(
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Incoming webhook ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">update_incoming_webhook</a>(...) -> IncomingWebhook</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially update an incoming webhook receiver. Provided top-level fields replace the existing values.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.update_incoming_webhook(
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Incoming webhook ID
    
</dd>
</dl>

<dl>
<dd>

**auth:** `typing.Optional[IncomingWebhookAuth]` 
    
</dd>
</dl>

<dl>
<dd>

**idempotency:** `typing.Optional[IdempotencyConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rules:** `typing.Optional[typing.List[IncomingWebhookRule]]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IncomingWebhookStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**target:** `typing.Optional[IncomingWebhookTarget]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">list_webhook_deliveries</a>(...) -> typing.List[WebhookDeliverySummary]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List delivery events for an incoming webhook, with optional status and date filters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.list_webhook_deliveries(
    webhook_id="webhook_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Incoming webhook ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[IngressEventStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.webhooks.<a href="src/islo/webhooks/client.py">get_webhook_delivery</a>(...) -> WebhookDeliveryDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get full detail for a single webhook delivery event, including a truncated body preview and action attempts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    api_version="<X-Islo-Api-Version>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.get_webhook_delivery(
    webhook_id="webhook_id",
    event_id="event_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**webhook_id:** `str` — Incoming webhook ID
    
</dd>
</dl>

<dl>
<dd>

**event_id:** `str` — Delivery event ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

