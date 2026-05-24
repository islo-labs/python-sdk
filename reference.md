# Reference
## auth
<details><summary><code>client.auth.<a href="src/islo/auth/client.py">exchange_access_key</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange a Descope access key for a session JWT. No authentication required.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.auth.exchange_access_key(
    access_key="access_key",
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

**access_key:** `str` — Descope access key to exchange for a session JWT
    
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

## Sandboxes
<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_exec_sessions</a>(...) -> typing.List[ExecSessionResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all exec sessions for a sandbox.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.list_exec_sessions(
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

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Only return sessions with activity at or after this timestamp
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_exec_session_asciinema</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return logs for a specific exec session in asciinema v2 format for playback.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_exec_session_asciinema(
    sandbox_id="sandbox_id",
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

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of log lines
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_exec_session_logs</a>(...) -> ExecLogsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return raw logs for a specific exec session.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_exec_session_logs(
    sandbox_id="sandbox_id",
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

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of log lines
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Only return logs after this timestamp
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_agent_sessions</a>(...) -> typing.List[AgentSessionResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all Claude agent sessions for a sandbox, ordered by most recent first.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.list_agent_sessions(
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

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Only return sessions with activity at or after this timestamp
    
</dd>
</dl>

<dl>
<dd>

**include_subagents:** `typing.Optional[bool]` — Include child/subagent sessions in addition to root sessions
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_agent_session_events</a>(...) -> typing.List[AgentSessionEventResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return all trace events for a specific agent session, ordered by timestamp.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_agent_session_events(
    sandbox_id="sandbox_id",
    session_name="session_name",
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

**sandbox_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_path:** `typing.Optional[str]` — Stable unique session path from the session list response. Use this to disambiguate duplicate session names.
    
</dd>
</dl>

<dl>
<dd>

**include_descendants:** `typing.Optional[bool]` — When true, include descendant subagent sessions under the requested session
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size — number of events to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of events to skip (for pagination)
    
</dd>
</dl>

<dl>
<dd>

**since:** `typing.Optional[datetime.datetime]` — Only return events after this timestamp (exclusive). Applied before offset.
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_sandboxes</a>(...) -> PaginatedSandboxResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**status:** `typing.Optional[str]` 
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**init_capabilities:** `typing.Optional[typing.List[InitCapability]]` 
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_sandbox</a>(...) -> SandboxResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.get_sandbox(
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

**name:** `str` — Sandbox name
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.delete_sandbox(
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_exec_interactive</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_exec_interactive(
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_exec_stream</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_exec_stream(
    name="name",
    args=[
        "args"
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**args:** `typing.List[str]` — Command and arguments to execute (e.g., ["/entrypoint.sh"])
    
</dd>
</dl>

<dl>
<dd>

**env_vars:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Optional environment variables to pass to the command
    
</dd>
</dl>

<dl>
<dd>

**timeout_secs:** `typing.Optional[int]` — Accepted but ignored (CLI sends this field).
    
</dd>
</dl>

<dl>
<dd>

**user:** `typing.Optional[str]` — User to run the command as (e.g., "islo"). If not specified, uses image default.
    
</dd>
</dl>

<dl>
<dd>

**workdir:** `typing.Optional[str]` — Working directory for the command. If not specified, uses the image's WorkingDir (from Dockerfile).
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_download_file</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_download_file(
    name="name",
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_upload_file</a>(...) -> FileUploadStatusResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_upload_file(
    name="name",
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_download_archive</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_download_archive(
    name="name",
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_upload_archive</a>(...) -> FileUploadStatusResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_upload_archive(
    name="name",
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_pause</a>(...) -> SandboxResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_pause(
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_port_forward</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_port_forward(
    name="name",
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` — Target port inside the sandbox VM
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_promote_cache</a>(...) -> PromoteCacheResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_promote_cache(
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_proxy_root</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_proxy_root(
    name="name",
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` — Target port inside the sandbox VM
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_proxy</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_proxy(
    name="name",
    port=1,
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` — Target port inside the sandbox VM
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Path suffix forwarded to the VM
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_resume</a>(...) -> SandboxResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_resume(
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_save_snapshot</a>(...) -> SaveSnapshotResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_save_snapshot(
    name="name",
    presigned_url="presigned_url",
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**presigned_url:** `str` 
    
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">sandbox_ws_proxy</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sandboxes.sandbox_ws_proxy(
    name="name",
    port=1,
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**port:** `int` — Target port inside the sandbox VM
    
</dd>
</dl>

<dl>
<dd>

**path:** `typing.Optional[str]` — Optional path suffix forwarded to the VM
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

List available preset providers and their pre-provisioned Descope apps.

The ``apps`` array carries every (auth_method, scope) -> app_id combo a
preset supports, so the modal can resolve the right ``app_id`` locally
and skip a server round-trip on the connect path.
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**cloud_role:** `typing.Optional[str]` — Cloud role name or public_id
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**cloud_role:** `typing.Optional[str]` — Cloud role name or public_id, empty string to unset
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**content_filter:** `typing.Optional[ContentFilterSchema]` 
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**content_filter:** `typing.Optional[ContentFilterSchema]` 
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

## Sessions
<details><summary><code>client.sessions.<a href="src/islo/sessions/client.py">sandbox_list_sessions</a>(...) -> ListSessionsResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sessions.sandbox_list_sessions(
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sessions.<a href="src/islo/sessions/client.py">sandbox_create_session</a>(...) -> CreateSessionResponse</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sessions.sandbox_create_session(
    name="name",
    create_session_request_name="name",
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

**name:** `str` — Sandbox name
    
</dd>
</dl>

<dl>
<dd>

**create_session_request_name:** `str` 
    
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

<details><summary><code>client.sessions.<a href="src/islo/sessions/client.py">sandbox_kill_session</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sessions.sandbox_kill_session(
    name="name",
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.sessions.<a href="src/islo/sessions/client.py">sandbox_attach_session</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.sessions.sandbox_attach_session(
    name="name",
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

**name:** `str` — Sandbox name
    
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

## Shares
<details><summary><code>client.shares.<a href="src/islo/shares/client.py">list_shares</a>(...) -> typing.List[ShareResponse]</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.shares.list_shares(
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

**name:** `str` — Sandbox name
    
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

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from islo import Islo
from islo.environment import IsloEnvironment

client = Islo(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.shares.create_share(
    name="name",
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

**name:** `str` — Sandbox name
    
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

<details><summary><code>client.shares.<a href="src/islo/shares/client.py">delete_share</a>(...)</code></summary>
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.shares.delete_share(
    name="name",
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

**name:** `str` — Sandbox name
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=IsloEnvironment.PRODUCTION,
)

client.snapshots.create_snapshot(
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

**sandbox_id:** `str` 
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**name:** `str` — Name
    
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
    client_id="<clientId>",
    client_secret="<clientSecret>",
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

**name:** `str` — Name
    
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

