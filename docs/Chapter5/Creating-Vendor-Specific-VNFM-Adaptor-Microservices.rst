.. Modifications Copyright © 2017-2018 AT&T Intellectual Property.

.. Licensed under the Creative Commons License, Attribution 4.0 Intl.
   (the "License"); you may not use this documentation except in compliance
   with the License. You may obtain a copy of the License at

.. https://creativecommons.org/licenses/by/4.0/

.. Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Creating Vendor-Specific VNFM Adaptor Microservices
---------------------------------------------------

VNFs can be managed by vendor-specific VNFMs. To add a vendor-specific
VNFM to ONAP, a vendor-specific VNFM adaptor is added to ONAP implementing
the interface of the vendor-specific VNFM.

A vendor-specific VNFM adaptor is a microservice with a unique name and
an appointed port. When started up, the vendor-specific VNFM adaptor
microservice is automatically registered to the Microservices Bus (MSB).
The following RESTful example describes the scenario of registering a
vendor-specific VNFM adaptor to MSB:

.. code-block:: java

    POST /api/microservices/v1/services
    {
        "serviceName": "catalog",
        "version": "v1",
        "url": "/api/catalog/v1",
        "protocol": "REST",
        "visualRange": "1",
        "nodes": [
        {
            "ip": "10.74.56.36",
            "port": "8988",
            "ttl": 0
        }
        ]
    }
