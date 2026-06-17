# Reference
## tenants
<details><summary><code>client.tenants.<a href="src/islo/tenants/client.py">list_tenant_compute_regions</a>() -> TenantRegionsResponse</code></summary>
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

## integrations
<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integration_providers</a>() -> IntegrationProvidersResponse</code></summary>
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

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integrations</a>() -> IntegrationListResponse</code></summary>
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

<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_custom_services</a>() -> CustomServicesResponse</code></summary>
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

Disconnect a custom integration by its Descope app ID.

Authorization is by deterministic-ID prefix: only apps whose ID matches
``cust-{tenant-prefix}-`` are accepted, which scopes the operation to the
caller's workspace without a DB lookup. ``scope`` selects which side's
tokens to revoke (per-user vs tenant-wide); ``delete_app=true`` removes
the Descope app entirely (affects every user in the workspace).
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
    environment=IsloEnvironment.PRODUCTION,
)

client.integrations.disconnect_custom_integration(
    descope_app_id="descope_app_id",
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

**descope_app_id:** `str` 
    
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

## gateway-profiles
<details><summary><code>client.gateway_profiles.<a href="src/islo/gateway_profiles/client.py">list_gateway_profiles</a>() -> typing.List[GatewayProfileResponse]</code></summary>
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

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_action:** `typing.Optional[GatewayAction]` 
    
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

**cloud_role:** `typing.Optional[str]` — Cloud role public ID (UUID)
    
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

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**default_action:** `typing.Optional[GatewayAction]` 
    
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

**cloud_role:** `typing.Optional[str]` — Cloud role public ID (UUID), empty string to unset
    
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

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**path_pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**methods:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[GatewayAction]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_rpm:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_key:** `typing.Optional[str]` 
    
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

**priority:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**host_pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**path_pattern:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**methods:** `typing.Optional[typing.List[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[GatewayAction]` 
    
</dd>
</dl>

<dl>
<dd>

**rate_limit_rpm:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**provider_key:** `typing.Optional[str]` 
    
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
    environment=IsloEnvironment.PRODUCTION,
)

client.gateway_profiles.reorder_gateway_rules(
    profile_id="profile_id",
    rules=[
        RuleReorderItem(
            rule_id="rule_id",
            priority=1,
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

## CloudRoles
<details><summary><code>client.cloud_roles.<a href="src/islo/cloud_roles/client.py">list_cloud_roles</a>() -> typing.List[CloudRoleResponse]</code></summary>
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
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    environment=IsloEnvironment.PRODUCTION,
)

client.cloud_roles.create_cloud_role(
    provider="aws",
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

**is_enabled:** `typing.Optional[bool]` 
    
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

Create a new sandbox for the authenticated tenant.
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

**snapshot_url:** `typing.Optional[str]` 
    
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

**command:** `typing.List[str]` — Command to execute.
    
</dd>
</dl>

<dl>
<dd>

**env:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Environment variables to inject into this execution session.
    
</dd>
</dl>

<dl>
<dd>

**timeout_secs:** `typing.Optional[int]` — Optional client-side timeout hint. Currently accepted for API compatibility.
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — User to run the command as (e.g., "islo"). If not provided, uses image default.
    
</dd>
</dl>

<dl>
<dd>

**workdir:** `typing.Optional[str]` — Working directory for command execution inside the sandbox.
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">download_file</a>(...)</code></summary>
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
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.upload_file(
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

**path:** `str` — Destination path inside the sandbox
    
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
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.upload_archive(
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

**path:** `str` — Destination directory inside the sandbox
    
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

Create a snapshot from a running sandbox.
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
from islo import Islo, IncomingWebhookAuthZero
from islo.environment import IsloEnvironment

client = Islo(
    api_key="<token>",
    environment=IsloEnvironment.PRODUCTION,
)

client.webhooks.create_incoming_webhook(
    auth=IncomingWebhookAuthZero(
        auth_type="none",
    ),
    idempotency={
        "source": "header",
        "name": "name"
    },
    name="name",
    target={
        "target_type": "fixed_sandbox_name",
        "sandbox_name": "sandbox_name"
    },
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

