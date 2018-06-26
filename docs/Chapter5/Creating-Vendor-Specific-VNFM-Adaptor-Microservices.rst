.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. http://creativecommons.org/licenses/by/4.0
.. Copyright 2017 AT&T Intellectual Property.  All rights reserved.

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
