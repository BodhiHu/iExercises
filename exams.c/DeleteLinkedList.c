#include "stdio.h"
#include "stdlib.h"

typedef struct _Node {
  int value;
  struct _Node* next;
} Node;

Node* DeleteDuplication(Node* listHead) {
  if (listHead == NULL) {
    return listHead;
  }

  Node* trimedList = NULL;
  Node* trimedListCurrent = NULL;

  Node* curNode = listHead;
  int currrentDuplidateValue = -1;

  while (curNode != NULL) {
    if ((curNode->next == NULL || curNode->value != curNode->next->value) && curNode->value != currrentDuplidateValue) {
      if (trimedListCurrent == NULL) {
        trimedListCurrent = curNode;
      }
      if (trimedList == NULL) {
        trimedList = trimedListCurrent;
      }
      if (trimedListCurrent != curNode) {
        trimedListCurrent->next = curNode;
        trimedListCurrent = curNode->next;
      }
      currrentDuplidateValue = -1;
    } else {
      currrentDuplidateValue = curNode->value;
    }

    curNode = curNode->next;
  }

  return trimedList;
}
