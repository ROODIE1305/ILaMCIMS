const customerListElement = document.getElementById("customers-list");
const addCustomerForm = document.getElementById("add-customer-form");
const updateCustomerForm = document.getElementById("update-customer-form");

// Function to fetch and display all customers
async function getCustomers() {
  try {
    const response = await fetch("/customers");
    const customers = await response.json();
    customerListElement.innerHTML = ""; // Clear previous list

    customers.forEach((customer) => {
      const customerElement = document.createElement("div");
      customerElement.innerHTML = `
        <h3>${customer.name}</h3>
        <p>Email: ${customer.email}</p>
        <p>Phone: ${customer.phone}</p>
        <p>Address: <span class="math-inline">\{customer\.address\}</p\>
<button data\-customer\-id\="</span>{customer.customer_id}" onclick="editCustomer(event)">Edit</button>
        <button data-customer-id="${customer.customer_id}" onclick="deleteCustomer(event)">Delete</button>
      `;
      customerListElement.appendChild(customerElement);
    });
  } catch (error) {
    console.error(error);
    alert("Error fetching customers!");
  }
}

// Function to handle adding a new customer
addCustomerForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const phone = document.getElementById("phone").value;
  const address = document.getElementById("address").value;

  try {
    const response = await fetch("/customers", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, phone, address }),
    });

    if (!response.ok) {
      throw new Error("Failed to add customer");
    }

    const newCustomer = await response.json();
    alert(`Customer ${newCustomer.name} added successfully!`);
    getCustomers();
    addCustomerForm.reset();
  } catch (error) {
    console.error(error);
    alert("Error adding customer!");
  }
});

// Function to pre-fill update