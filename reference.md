# Reference
## sandboxes
<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_sandboxes</a>(...) -> PaginatedSandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List and filter sandboxes for the authenticated tenant.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**search:** `typing.Optional[str]` — Search by sandbox name (case-insensitive)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.List[str]]` — Filter by status (e.g., ?status=running&status=unknown&status=deleted)
    
</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[datetime.datetime]` — Filter sandboxes created on or after this date
    
</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[datetime.datetime]` — Filter sandboxes created on or before this date
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` — Filter by creator. Use 'me' for your own sandboxes.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max items per page
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip
    
</dd>
</dl>

<dl>
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

Create a new sandbox with the specified configuration.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**name:** `typing.Optional[str]` — User-friendly sandbox name. If omitted, a random slug is generated.
    
</dd>
</dl>

<dl>
<dd>

**image:** `typing.Optional[str]` — Container image to use
    
</dd>
</dl>

<dl>
<dd>

**vcpus:** `typing.Optional[int]` — Number of vCPUs
    
</dd>
</dl>

<dl>
<dd>

**memory_mb:** `typing.Optional[int]` — Memory in MB
    
</dd>
</dl>

<dl>
<dd>

**disk_gb:** `typing.Optional[int]` — Disk size in GB
    
</dd>
</dl>

<dl>
<dd>

**cache_key:** `typing.Optional[str]` — Tool cache key for golden cache lookup (computed by CLI)
    
</dd>
</dl>

<dl>
<dd>

**env:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` — Environment variables to inject into the sandbox
    
</dd>
</dl>

<dl>
<dd>

**workdir:** `typing.Optional[str]` — Working directory relative to /workspace (e.g. 'my-project')
    
</dd>
</dl>

<dl>
<dd>

**init_capabilities:** `typing.Optional[typing.List[str]]` — Init capabilities to enable (in addition to Core which always runs). None = all capabilities (default, backward compatible), [] = Core only (minimal init), ['ssh', 'devtools'] = Core + specified capabilities. Valid values: ssh, terminal, devtools, docker.
    
</dd>
</dl>

<dl>
<dd>

**gateway_profile:** `typing.Optional[str]` — Gateway profile name or ID to apply. Uses tenant default if omitted.
    
</dd>
</dl>

<dl>
<dd>

**snapshot_name:** `typing.Optional[str]` — Name of a snapshot to restore from. When set, the VM is created from the snapshot's filesystem.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">get_sandbox_by_id_sandboxes_by_id_sandbox_id_get</a>(...) -> SandboxResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific sandbox by stable public ID, including deleted sandboxes.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.sandboxes.get_sandbox_by_id_sandboxes_by_id_sandbox_id_get(
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

Get details of a specific sandbox by name.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
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

Stop and permanently remove a sandbox.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
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

Stop a sandbox (destroy VM) but keep the record visible.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
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

Snapshot the sandbox VM state to disk and free CPU/memory. The sandbox can be resumed later.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
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

Resume a paused sandbox from its local snapshot.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">promote_sandbox_cache</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Promote the sandbox's tool cache to golden cache for reuse.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.sandboxes.promote_sandbox_cache(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">list_sessions</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List active persistent sessions (shpool) in a sandbox.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">create_session</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a persistent session in a sandbox.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.sandboxes.create_session(
    sandbox_name="sandbox_name",
    request={
        "key": "value"
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
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

Kill a persistent session in a sandbox.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
)

client.sandboxes.kill_session(
    sandbox_name="sandbox_name",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**session_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">download_file</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a single file from a sandbox.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Absolute source path in the sandbox
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">upload_file</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a single file into a sandbox.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Absolute target path in the sandbox
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">download_archive</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a directory from a sandbox as a tar.gz archive.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Absolute source directory in the sandbox
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">upload_archive</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a tar.gz archive and extract it into a sandbox directory.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**path:** `str` — Absolute target directory in the sandbox
    
</dd>
</dl>

<dl>
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

Execute a command inside a sandbox by name.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
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

Poll the result of a previously started exec command.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**exec_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sandboxes.<a href="src/islo/sandboxes/client.py">exec_in_sandbox_stream</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a command inside a sandbox and stream stdout/stderr as SSE.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

**sandbox_name:** `str` 
    
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

## Snapshots
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

## integrations
<details><summary><code>client.integrations.<a href="src/islo/integrations/client.py">list_integration_providers</a>() -> IntegrationProvidersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List available integration providers.

Returns provider names and their supported hosts.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

List all integrations for the current user and tenant.

Shows both user-level and tenant-level integrations.
User-level integrations take precedence in display.
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

client = Islo(
    api_key="<token>",
    base_url="https://yourhost.com/path/to/api",
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

